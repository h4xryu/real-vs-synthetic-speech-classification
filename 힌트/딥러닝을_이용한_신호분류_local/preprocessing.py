"""학부 실습용 음성 전처리.

음성 파일 -> mono 16 kHz -> 2초 길이 -> 로그멜 스펙트로그램 [40, 200]
"""

import csv
from pathlib import Path

import numpy as np
import soundfile as sf
import torch


# 프로젝트 모델이 기대하는 음성 표본화율과 입력 길이.
SAMPLE_RATE = 16000
DURATION_SECONDS = 2
SAMPLE_COUNT = SAMPLE_RATE * DURATION_SECONDS

# STFT 설정: 25 ms 창, 10 ms 이동, FFT 크기 512.
N_FFT = 512
WINDOW_LENGTH = 400
HOP_LENGTH = 160
FRAME_COUNT = SAMPLE_COUNT // HOP_LENGTH
MEL_COUNT = 40

# 같은 설정으로 모든 파일을 처리해 특징 크기를 일정하게 만든다.
WINDOW = torch.hann_window(WINDOW_LENGTH)


def make_mel_filterbank():
    """주파수 bins를 40개 멜 대역으로 묶는 삼각 필터를 만든다."""
    # Hertz와 Mel 사이를 변환한다. Mel 간격은 낮은 주파수를 더 자세히 나눈다.
    def hz_to_mel(frequency):
        return 2595.0 * np.log10(1.0 + frequency / 700.0)

    def mel_to_hz(mel):
        return 700.0 * (10.0 ** (mel / 2595.0) - 1.0)

    # 0 Hz부터 Nyquist 주파수까지 필터의 왼쪽·가운데·오른쪽 경계를 만든다.
    mel_edges = np.linspace(
        hz_to_mel(0.0),
        hz_to_mel(SAMPLE_RATE / 2),
        MEL_COUNT + 2,
    )
    hz_edges = mel_to_hz(mel_edges)
    frequencies = np.linspace(0.0, SAMPLE_RATE / 2, N_FFT // 2 + 1)

    # 각 삼각 필터는 중심 주파수에서 1, 양쪽 경계에서 0이 된다.
    low = hz_edges[:-2, None]
    center = hz_edges[1:-1, None]
    high = hz_edges[2:, None]
    filters = np.maximum(
        0.0,
        np.minimum(
            (frequencies - low) / (center - low),
            (high - frequencies) / (high - center),
        ),
    )

    # STFT 행렬과 곱할 수 있도록 PyTorch tensor로 바꾼다.
    return torch.tensor(filters, dtype=torch.float32)


# 모든 파일에서 재사용할 멜 필터 뱅크.
MEL_FILTERBANK = make_mel_filterbank()


def load_audio(path):
    """파일을 mono 16 kHz float32 음성으로 읽는다."""
    audio, sample_rate = sf.read(path, always_2d=False, dtype="float32")

    # 스테레오라면 좌우 채널의 평균을 사용해 하나의 음성 신호로 만든다.
    if audio.ndim > 1:
        audio = audio.mean(axis=1)

    # 모델 표본화율이 다르면 시간축 길이를 맞춰 16 kHz로 변환한다.
    if sample_rate != SAMPLE_RATE:
        new_length = int(round(len(audio) * SAMPLE_RATE / sample_rate))
        audio = np.interp(
            np.linspace(0, len(audio), new_length, endpoint=False),
            np.arange(len(audio)),
            audio,
        )

    # 이후 PyTorch 연산에 맞는 float32로 반환한다.
    return np.asarray(audio, dtype=np.float32)


def fixed_length(audio):
    """짧은 음성은 0으로 채우고, 긴 음성은 앞 2초만 사용한다."""
    if len(audio) < SAMPLE_COUNT:
        audio = np.pad(audio, (0, SAMPLE_COUNT - len(audio)))
    return audio[:SAMPLE_COUNT].astype(np.float32)


def log_mel(audio):
    """2초 음성을 모델 입력 [40 멜 대역, 200 시간 프레임]으로 바꾼다."""
    # 고정된 2초 길이인지 확인해 모든 파일의 입력 크기를 같게 한다.
    audio = fixed_length(audio)

    # STFT는 짧은 구간마다 주파수 에너지를 계산한다.
    spectrum = torch.stft(
        torch.from_numpy(audio),
        n_fft=N_FFT,
        hop_length=HOP_LENGTH,
        win_length=WINDOW_LENGTH,
        window=WINDOW,
        return_complex=True,
    )

    # 복소수 STFT에서 power를 얻고, 멜 필터로 40개 대역에 모은다.
    power = spectrum.abs().pow(2)
    mel_power = MEL_FILTERBANK @ power

    # 로그는 에너지 범위를 압축해 작은 값과 큰 값의 차이를 줄인다.
    features = torch.log(mel_power.clamp_min(1e-6))

    # 중심 패딩 때문에 생기는 여분 프레임을 제외해 정확히 200개를 맞춘다.
    return features[:, :FRAME_COUNT]


def read_dataset(csv_path):
    """목록 CSV와 음성을 읽어 (특징, 정수 라벨, 파일 이름)을 반환한다."""
    csv_path = Path(csv_path)

    # CSV의 경로는 CSV 파일이 있는 dataset 폴더를 기준으로 해석한다.
    with csv_path.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        raise ValueError(f"목록에 음성이 없습니다: {csv_path}")

    # 프로젝트에서 사용하는 클래스 이름과 순서를 고정한다.
    labels = ["original", "TTS", "voice_conversion", "sovits"]
    features = []
    targets = []
    filenames = []
    missing = []

    # 음성 한 개마다 전처리하고 정답 라벨을 숫자로 바꾼다.
    for row in rows:
        audio_path = csv_path.parent / row["path"]
        if not audio_path.is_file():
            missing.append(audio_path)
            continue

        label = row.get("label", "")
        if label not in labels:
            raise ValueError(f"알 수 없는 라벨 {label!r}: {csv_path}")

        audio = load_audio(audio_path)
        features.append(log_mel(audio))
        targets.append(labels.index(label))
        filenames.append(Path(row["path"]).name)

    # 빠진 파일을 숨기지 않고 모두 알려준다.
    if missing:
        examples = ", ".join(str(path) for path in missing[:3])
        raise FileNotFoundError(f"음성 {len(missing)}개를 찾지 못했습니다. 예: {examples}")

    # 배치 학습에 사용할 [파일 수, 40, 200] tensor와 정답 tensor를 만든다.
    x = torch.stack(features)
    y = torch.tensor(targets, dtype=torch.long)
    return x, y, filenames
