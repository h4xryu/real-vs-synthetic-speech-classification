

import torch
import torch.nn as nn
import torch.nn.functional as F



class INCONV(nn.Module):
    """ResU2D-LC 첫 단계: 입력의 시간·주파수 패턴을 특징 채널로 바꾼다."""

    def __init__(self, in_ch, out_ch):
        super().__init__()

        # 시간 방향으로 간격을 줄이고 여러 종류의 특징 지도를 만든다.
        self.conv = nn.Conv2d(
            in_channels=in_ch,
            out_channels=out_ch,
            kernel_size=(3, 15),
            stride=(1, 2),
            padding=(1, 7),
            bias=False,
        )
        self.bn = nn.BatchNorm2d(out_ch)

    def forward(self, x):
        return F.leaky_relu(self.bn(self.conv(x)))


class ResUBlock(nn.Module):
    """U자형 인코더-디코더와 잔차 연결로 여러 시간 크기의 특징을 학습한다."""

    def __init__(self, out_ch, mid_ch, layers, downsampling=True):
        super().__init__()
        self.downsampling = downsampling

        # 블록 입력을 먼저 정리한다. 마지막에 이 결과를 잔차로 더한다.
        self.input_conv = nn.Conv2d(
            out_ch, out_ch, kernel_size=(3, 9), padding=(1, 4), bias=False
        )
        self.input_bn = nn.BatchNorm2d(out_ch)

        # 인코더는 시간축 크기를 단계마다 줄이며 넓은 문맥을 모은다.
        self.encoders = nn.ModuleList()
        for layer_index in range(layers):
            input_channels = out_ch if layer_index == 0 else mid_ch
            self.encoders.append(nn.Sequential(
                nn.Conv2d(
                    input_channels,
                    mid_ch,
                    kernel_size=(3, 9),
                    stride=(1, 2),
                    padding=(1, 4),
                    bias=False,
                ),
                nn.BatchNorm2d(mid_ch),
                nn.LeakyReLU(),
            ))

        # 병목층은 가장 작은 시간 해상도에서 중요한 패턴을 조합한다.
        self.bottleneck = nn.Sequential(
            nn.Conv2d(mid_ch, mid_ch, kernel_size=(3, 9), padding=(1, 4), bias=False),
            nn.BatchNorm2d(mid_ch),
            nn.LeakyReLU(),
        )

        # 디코더는 시간 해상도를 되돌린다.
        # 각 층에서 같은 해상도의 인코더 결과(skip)를 붙여 세부 정보를 보존한다.
        self.decoders = nn.ModuleList()
        for layer_index in range(layers):
            output_channels = out_ch if layer_index == layers - 1 else mid_ch
            self.decoders.append(nn.Sequential(
                nn.ConvTranspose2d(
                    mid_ch * 2,
                    output_channels,
                    kernel_size=(3, 9),
                    stride=(1, 2),
                    padding=(1, 4),
                    output_padding=(0, 1),
                    bias=False,
                ),
                nn.BatchNorm2d(output_channels),
                nn.LeakyReLU(),
            ))

        # 블록 사이 시간 크기를 줄여 뒤쪽 블록이 더 넓은 문맥을 본다.
        if downsampling:
            self.downsample = nn.Sequential(
                nn.AvgPool2d(kernel_size=(1, 2), stride=(1, 2)),
                nn.Conv2d(out_ch, out_ch, kernel_size=1, bias=False),
            )

    def forward(self, x):
        # 잔차로 보존할 블록 입력 특징을 계산한다.
        x_in = F.leaky_relu(self.input_bn(self.input_conv(x)))

        # 인코더 단계의 출력을 저장해 디코더의 skip 연결에 사용한다.
        encoded = []
        x = x_in
        for encoder in self.encoders:
            x = encoder(x)
            encoded.append(x)

        # 가장 압축된 특징을 한 번 더 조합한다.
        x = self.bottleneck(x)

        # 깊은 곳부터 디코더를 실행하고 같은 크기의 인코더 특징을 붙인다.
        for decoder_index, decoder in enumerate(self.decoders):
            skip = encoded[-1 - decoder_index]

            # 홀수 길이에서도 두 특징의 시간 크기를 맞춘다.
            x = x[..., :skip.size(-1)]
            x = decoder(torch.cat((x, skip), dim=1))

        # 입력과 출력의 시간 크기를 맞춘 뒤 잔차 연결로 원래 특징을 더한다.
        x = x[..., :x_in.size(-1)] + x_in

        # 다음 블록을 위한 시간축 축소. 마지막 블록이면 그대로 반환한다.
        if self.downsampling:
            x = self.downsample(x)
        return x


class ChannelMixer(nn.Module):
    """시간·주파수 축을 각각 모아 고정 길이 벡터로 합친다."""

    def __init__(self, out_ch):
        super().__init__()

        # 시간축을 따라 각 주파수 채널의 중요한 응답을 모은다.
        self.time_conv = nn.Conv1d(out_ch, out_ch, kernel_size=1, bias=False)
        self.time_bn = nn.BatchNorm1d(out_ch)

        # 주파수축을 따라 각 시간 구간의 중요한 응답을 모은다.
        self.freq_conv = nn.Conv1d(out_ch, out_ch, kernel_size=1, bias=False)
        self.freq_bn = nn.BatchNorm1d(out_ch)

    def forward(self, x):
        # 주파수축을 최댓값으로 모아 시간별 특징을 만든다.
        time_features = x.amax(dim=2)
        time_features = F.leaky_relu(self.time_bn(self.time_conv(time_features)))
        time_features = F.adaptive_max_pool1d(time_features, 1).squeeze(-1)

        # 시간축을 최댓값으로 모아 주파수별 특징을 만든다.
        freq_features = x.amax(dim=3)
        freq_features = F.leaky_relu(self.freq_bn(self.freq_conv(freq_features)))
        freq_features = F.adaptive_max_pool1d(freq_features, 1).squeeze(-1)

        # 두 관점의 특징을 이어 붙여 분류기에 전달한다.
        return torch.cat((time_features, freq_features), dim=1)


class ResU2D_LC(nn.Module):
    """프로젝트 로그멜 입력 [batch, 40, frames]에 맞춘 ResU2D-LC 분류기."""

    def __init__(self, nOUT=4, in_ch=1, out_ch=128, mid_ch=64, bin=40):
        super().__init__()
        self.bin = bin

        # 입력 로그멜을 2D 합성곱이 처리할 수 있는 특징 채널로 바꾼다.
        self.inconv = INCONV(in_ch, out_ch)

        # 두 개의 U자 블록이 서로 다른 크기의 시간 패턴을 학습한다.
        self.rub_0 = ResUBlock(out_ch, mid_ch, layers=6)
        self.rub_1 = ResUBlock(out_ch, mid_ch, layers=5)

        # 시간과 주파수 특징을 각각 모아 하나의 벡터로 만든다.
        self.channel_mixer = ChannelMixer(out_ch)

        # 최종 벡터를 클래스별 점수 nOUT개로 바꾼다.
        self.classifier = nn.Linear(out_ch * 2, nOUT)

    def forward(self, x):
        # 잘못된 입력 모양은 조용히 진행하지 않고 이해하기 쉬운 오류로 알린다.
        if x.ndim != 3 or x.size(1) != self.bin:
            raise ValueError(
                f"입력은 [batch, {self.bin}, frames]여야 합니다. "
                f"현재 모양: {tuple(x.shape)}"
            )

        # 채널 차원을 추가한 뒤 입력층과 U자 블록을 통과시킨다.
        x = self.inconv(x.unsqueeze(1))
        x = self.rub_0(x)
        x = self.rub_1(x)

        # 특징을 모아 최종 클래스 점수를 출력한다.
        return self.classifier(self.channel_mixer(x))
