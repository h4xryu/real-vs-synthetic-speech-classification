
"""DNN 예시의 입력 만들기와 모델 구조.

음성 2초 → 로그 멜 스펙트로그램 [40 멜 대역, 200 프레임]
        → ResU2D_LC → 라벨 4개 점수

train.py와 validation.py에서 공통으로 사용한다.
"""

import numpy as np
import soundfile as sf
import torch
import torch.nn as nn

from math import gcd
from scipy.signal import resample_poly

from common import LABELS, read_list


# =========================================
# 전처리 부분
# =========================================

SR = 16000
SAMPLES = SR * 2

N_FFT = 512
WINDOW_LENGTH = 400
HOP_LENGTH = 160

N_MELS = 40
FRAME_COUNT = SAMPLES // HOP_LENGTH

# 모든 음성에 동일하게 사용하는 Hann Window.
WINDOW = torch.hann_window(WINDOW_LENGTH, periodic=True)


def mel_filterbank(n_mels=N_MELS, n_fft=N_FFT, sr=SR):
    """HTK Mel Scale 기반 삼각 필터 [n_mels, n_fft//2+1] 생성."""

    hz2mel = lambda f: 2595.0 * np.log10(1.0 + f / 700.0)
    mel2hz = lambda m: 700.0 * (10.0 ** (m / 2595.0) - 1.0)

    edges = mel2hz(
        np.linspace(
            hz2mel(0.0),
            hz2mel(sr / 2),
            n_mels + 2,
        )
    )

    freqs = np.linspace(
        0.0,
        sr / 2,
        n_fft // 2 + 1,
    )

    lo = edges[:-2, None]
    mid = edges[1:-1, None]
    hi = edges[2:, None]

    filters = np.maximum(
        0.0,
        np.minimum(
            (freqs - lo) / (mid - lo),
            (hi - freqs) / (hi - mid),
        ),
    )

    return torch.tensor(filters, dtype=torch.float32)


# 모든 음성에서 재사용하는 Mel Filterbank.
MEL_FB = mel_filterbank()


def load_audio(path):
    """음성 파일을 Mono 16 kHz float32로 변환한다."""

    audio, sr = sf.read(
        path,
        always_2d=False,
        dtype="float32",
    )

    audio = np.asarray(audio, dtype=np.float32)

    # 빈 파일 검사.
    if audio.size == 0:
        raise ValueError(f"빈 음성 파일입니다: {path}")

    # NaN 및 Inf 검사.
    if not np.isfinite(audio).all():
        raise ValueError(f"유효하지 않은 샘플이 있습니다: {path}")

    # Stereo를 Mono로 변환.
    if audio.ndim > 1:
        if audio.ndim != 2:
            raise ValueError(f"지원하지 않는 음성 형태입니다: {audio.shape}")

        audio = audio.mean(axis=1, dtype=np.float32)

    if sr <= 0:
        raise ValueError(f"잘못된 샘플링 주파수입니다: {sr}")

    # 16 kHz가 아니라면 Anti-aliasing 필터를 포함하여 리샘플링.
    if sr != SR:
        divisor = gcd(int(sr), SR)

        up = SR // divisor
        down = int(sr) // divisor

        audio = resample_poly(
            audio,
            up=up,
            down=down,
        )

    return np.asarray(audio, dtype=np.float32)


def fixed_length(audio):
    """음성 길이를 정확히 2초로 맞춘다."""

    if len(audio) < SAMPLES:
        audio = np.pad(
            audio,
            (0, SAMPLES - len(audio)),
            mode="constant",
        )

    return np.asarray(
        audio[:SAMPLES],
        dtype=np.float32,
    )


def load_fixed(path):
    """음성 파일을 읽어 Mono 16 kHz, 2초 길이로 반환한다."""

    audio = load_audio(path)
    return fixed_length(audio)


def logmel(audio):
    """2초 음성을 로그 멜 스펙트로그램 [40, 200]으로 변환한다."""

    audio = fixed_length(audio)

    # STFT 계산.
    spec = torch.stft(
        torch.from_numpy(audio),
        n_fft=N_FFT,
        hop_length=HOP_LENGTH,
        win_length=WINDOW_LENGTH,
        window=WINDOW,
        center=True,
        pad_mode="reflect",
        return_complex=True,
    )

    # Power Spectrogram.
    power = spec.abs().pow(2)

    # Mel Filterbank 적용.
    mel_power = MEL_FB @ power

    # 로그 변환.
    features = torch.log(
        mel_power.clamp_min(1e-6)
    )

    # 201개 프레임 중 앞의 200개 사용.
    features = features[:, :FRAME_COUNT]

    if features.shape != (N_MELS, FRAME_COUNT):
        raise RuntimeError(
            f"잘못된 특징 크기: {tuple(features.shape)}"
        )

    return features


def read_table(list_csv):
    """목록 CSV를 읽어 (특징, 정수 라벨, 파일 이름)을 반환한다."""

    rows = read_list(list_csv)

    if not rows:
        raise ValueError(f"목록에 음성이 없습니다: {list_csv}")

    # 모든 음성을 동일한 전처리로 변환.
    x = torch.stack([
        logmel(load_fixed(path))
        for path, _, _ in rows
    ]).contiguous()

    # 기존 common.LABELS의 클래스 순서 유지.
    labels = [
        label
        for _, _, label in rows
    ]

    y = (
        torch.tensor(
            [LABELS.index(label) for label in labels],
            dtype=torch.long,
        )
        if all(labels)
        else None
    )

    filenames = [
        name
        for _, name, _ in rows
    ]

    return x, y, filenames


# =========================================
# Model 구조 (변경하지 않음)
# =========================================


class INCONV(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()

        self.conv = nn.Conv2d(
            in_ch,
            out_ch,
            kernel_size=(3, 15),
            stride=(1, 2),
            padding=(1, 7),
            bias=False,
        )

        self.bn = nn.BatchNorm2d(out_ch)

    def forward(self, x):
        return torch.nn.functional.leaky_relu(
            self.bn(self.conv(x))
        )


class ResUBlock(nn.Module):
    def __init__(self, out_ch, mid_ch, layers, downsampling=True):
        super().__init__()

        self.downsampling = downsampling

        self.conv = nn.Conv2d(
            out_ch,
            out_ch,
            kernel_size=(3, 9),
            padding=(1, 4),
            bias=False,
        )

        self.bn = nn.BatchNorm2d(out_ch)

        self.encoders = nn.ModuleList()
        self.decoders = nn.ModuleList()

        for idx in range(layers):
            in_channels = out_ch if idx == 0 else mid_ch

            self.encoders.append(nn.Sequential(
                nn.Conv2d(
                    in_channels,
                    mid_ch,
                    kernel_size=(3, 9),
                    stride=(1, 2),
                    padding=(1, 4),
                    bias=False,
                ),
                nn.BatchNorm2d(mid_ch),
                nn.LeakyReLU(),
            ))

            out_channels = out_ch if idx == layers - 1 else mid_ch

            self.decoders.append(nn.Sequential(
                nn.ConvTranspose2d(
                    mid_ch * 2,
                    out_channels,
                    kernel_size=(3, 9),
                    stride=(1, 2),
                    padding=(1, 4),
                    output_padding=(0, 1),
                    bias=False,
                ),
                nn.BatchNorm2d(out_channels),
                nn.LeakyReLU(),
            ))

        self.bottleneck = nn.Sequential(
            nn.Conv2d(
                mid_ch,
                mid_ch,
                kernel_size=(3, 9),
                padding=(1, 4),
                bias=False,
            ),
            nn.BatchNorm2d(mid_ch),
            nn.LeakyReLU(),
        )

        if downsampling:
            self.idfunc = nn.Sequential(
                nn.AvgPool2d(
                    kernel_size=(1, 2),
                    stride=(1, 2),
                ),
                nn.Conv2d(
                    out_ch,
                    out_ch,
                    kernel_size=1,
                    bias=False,
                ),
            )

    def forward(self, x):
        x_in = torch.nn.functional.leaky_relu(
            self.bn(self.conv(x))
        )

        out = x_in
        encoder_out = []

        for layer in self.encoders:
            out = layer(out)
            encoder_out.append(out)

        out = self.bottleneck(out)

        for idx, layer in enumerate(self.decoders):
            skip = encoder_out[-1 - idx]
            out = out[..., :skip.size(-1)]

            out = layer(
                torch.cat((out, skip), dim=1)
            )

        out = out[..., :x_in.size(-1)] + x_in

        return self.idfunc(out) if self.downsampling else out


class ChannelMixer(nn.Module):
    """시간 축과 멜 주파수 축을 각각 고정 크기 벡터로 변환한다."""

    def __init__(self, out_ch):
        super().__init__()

        self.time_conv = nn.Conv1d(
            out_ch,
            out_ch,
            kernel_size=1,
            bias=False,
        )

        self.time_bn = nn.BatchNorm1d(out_ch)

        self.freq_conv = nn.Conv1d(
            out_ch,
            out_ch,
            kernel_size=1,
            bias=False,
        )

        self.freq_bn = nn.BatchNorm1d(out_ch)

    def forward(self, x):
        time = x.amax(dim=2)

        time = torch.nn.functional.leaky_relu(
            self.time_bn(self.time_conv(time))
        )

        time = torch.nn.functional.adaptive_max_pool1d(
            time,
            1,
        ).squeeze(-1)

        freq = x.amax(dim=3)

        freq = torch.nn.functional.leaky_relu(
            self.freq_bn(self.freq_conv(freq))
        )

        freq = torch.nn.functional.adaptive_max_pool1d(
            freq,
            1,
        ).squeeze(-1)

        return torch.cat((time, freq), dim=1)


class ResU2D_LC(nn.Module):
    """ResUNet-LC classifier for log-mel inputs [batch, 40, 200]."""

    def __init__(
        self,
        nOUT,
        in_ch=1,
        out_ch=128,
        mid_ch=64,
        lead=40,
    ):
        super().__init__()

        self.lead = lead

        self.inconv = INCONV(in_ch, out_ch)

        self.rub_0 = ResUBlock(
            out_ch,
            mid_ch,
            layers=6,
        )

        self.rub_1 = ResUBlock(
            out_ch,
            mid_ch,
            layers=5,
        )

        self.cm = ChannelMixer(out_ch)

        self.fc = nn.Linear(
            out_ch * 2,
            nOUT,
        )

    def forward(self, x):
        if x.ndim != 3 or x.size(1) != self.lead:
            raise ValueError(
                f"expected input shape [batch, {self.lead}, frames], "
                f"got {tuple(x.shape)}"
            )

        x = self.inconv(x.unsqueeze(1))
        x = self.rub_0(x)
        x = self.rub_1(x)

        return self.fc(self.cm(x))
