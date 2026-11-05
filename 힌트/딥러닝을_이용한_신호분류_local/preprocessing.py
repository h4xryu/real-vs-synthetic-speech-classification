
import csv
from pathlib import Path
from math import gcd

import numpy as np
import soundfile as sf
import torch
from scipy.signal import resample_poly


# =========================================
# 설정
# =========================================

SAMPLE_RATE = 16000
DURATION_SECONDS = 2
SAMPLE_COUNT = SAMPLE_RATE * DURATION_SECONDS

# STFT 설정: 25 ms 창, 10 ms 이동, FFT 크기 512.
N_FFT = 512
WINDOW_LENGTH = 400
HOP_LENGTH = 160

FRAME_COUNT = SAMPLE_COUNT // HOP_LENGTH
MEL_COUNT = 40

# 프로젝트에서 사용하는 클래스 순서.
LABELS = ["original", "TTS", "voice_conversion", "sovits"]

# 모든 파일에서 동일한 Hann Window 사용.
WINDOW = torch.hann_window(
    WINDOW_LENGTH,
    periodic=True
)


# =========================================
# Mel Filterbank
# =========================================

def make_mel_filterbank():
    """HTK Mel Scale 기반 삼각 필터 [40, 257] 생성."""

    def hz_to_mel(frequency):
        return 2595.0 * np.log10(1.0 + frequency / 700.0)

    def mel_to_hz(mel):
        return 700.0 * (10.0 ** (mel / 2595.0) - 1.0)

    # 0 Hz부터 Nyquist 주파수까지 42개 경계 생성.
    mel_edges = np.linspace(
        hz_to_mel(0.0),
        hz_to_mel(SAMPLE_RATE / 2),
        MEL_COUNT + 2,
    )

    hz_edges = mel_to_hz(mel_edges)

    frequencies = np.linspace(
        0.0,
        SAMPLE_RATE / 2,
        N_FFT // 2 + 1,
    )

    low = hz_edges[:-2, None]
    center = hz_edges[1:-1, None]
    high = hz_edges[2:, None]

    # 삼각형 형태의 Mel Filterbank.
    filters = np.maximum(
        0.0,
        np.minimum(
            (frequencies - low) / (center - low),
            (high - frequencies) / (high - center),
        ),
    )

    return torch.tensor(filters, dtype=torch.float32)


MEL_FILTERBANK = make_mel_filterbank()


# =========================================
# 음성 파일 읽기 및 리샘플링
# =========================================

def load_audio(path):
    """음성 파일을 mono 16 kHz float32로 변환한다."""

    audio, sample_rate = sf.read(
        path,
        always_2d=False,
        dtype="float32",
    )

    audio = np.asarray(audio, dtype=np.float32)

    # 빈 음성 파일 검사.
    if audio.size == 0:
        raise ValueError(f"빈 음성 파일입니다: {path}")

    # NaN 또는 Inf 검사.
    if not np.isfinite(audio).all():
        raise ValueError(f"유효하지 않은 샘플이 포함되어 있습니다: {path}")

    # Stereo 또는 다중 채널을 Mono로 변환.
    if audio.ndim > 1:
        if audio.ndim != 2:
            raise ValueError(f"지원하지 않는 음성 형태입니다: {audio.shape}")

        audio = audio.mean(axis=1, dtype=np.float32)

    # 샘플링 주파수 검사.
    if sample_rate <= 0:
        raise ValueError(f"잘못된 샘플링 주파수입니다: {sample_rate}")

    # 16 kHz가 아니면 Anti-aliasing 필터를 포함한 리샘플링.
    if sample_rate != SAMPLE_RATE:

        # 업샘플링 비율과 다운샘플링 비율을 최소 정수비로 계산.
        divisor = gcd(int(sample_rate), SAMPLE_RATE)

        up = SAMPLE_RATE // divisor
        down = int(sample_rate) // divisor

        audio = resample_poly(
            audio,
            up=up,
            down=down,
        )

    return np.asarray(audio, dtype=np.float32)


# =========================================
# 음성 길이 통일
# =========================================

def fixed_length(audio):
    """음성을 정확히 2초 길이로 맞춘다."""

    if len(audio) < SAMPLE_COUNT:
        # 부족한 길이는 0으로 채운다.
        audio = np.pad(
            audio,
            (0, SAMPLE_COUNT - len(audio)),
            mode="constant",
        )

    # 2초보다 긴 음성은 앞 2초만 사용한다.
    return np.asarray(
        audio[:SAMPLE_COUNT],
        dtype=np.float32,
    )


# =========================================
# Log-Mel Spectrogram
# =========================================

def log_mel(audio):
    """2초 음성을 [40, 200] 로그멜 스펙트로그램으로 변환한다."""

    audio = fixed_length(audio)

    # STFT 계산.
    spectrum = torch.stft(
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
    power = spectrum.abs().pow(2)

    # Mel Filterbank 적용.
    mel_power = MEL_FILTERBANK @ power

    # 로그 변환.
    features = torch.log(
        mel_power.clamp_min(1e-6)
    )

    # Center Padding으로 생성된 201개 프레임 중
    # 앞의 200개 프레임만 사용한다.
    features = features[:, :FRAME_COUNT]

    if features.shape != (MEL_COUNT, FRAME_COUNT):
        raise RuntimeError(
            f"잘못된 특징 크기: {tuple(features.shape)}"
        )

    return features


# =========================================
# Dataset 읽기
# =========================================

def read_dataset(csv_path):
    """CSV를 읽어 (특징, 정수 라벨, 파일 이름)을 반환한다."""

    csv_path = Path(csv_path)

    with csv_path.open(
        encoding="utf-8",
        newline="",
    ) as file:
        rows = list(csv.DictReader(file))

    if not rows:
        raise ValueError(f"목록에 음성이 없습니다: {csv_path}")

    features = []
    targets = []
    filenames = []
    missing = []

    # 파일 존재 여부 및 라벨 검사.
    for row in rows:
        relative_path = row.get("path", "").strip()
        label = row.get("label", "").strip()

        if not relative_path:
            raise ValueError(f"CSV에 파일 경로가 없습니다: {csv_path}")

        audio_path = csv_path.parent / relative_path

        if not audio_path.is_file():
            missing.append(audio_path)
            continue

        if label not in LABELS:
            raise ValueError(
                f"알 수 없는 라벨 {label!r}: {audio_path}"
            )

        audio_path = audio_path.resolve()

        # 음성 읽기 및 전처리.
        audio = load_audio(audio_path)
        feature = log_mel(audio)

        features.append(feature)
        targets.append(LABELS.index(label))
        filenames.append(Path(relative_path).name)

    # 누락된 파일이 있다면 데이터셋 생성 중단.
    if missing:
        examples = ", ".join(
            str(path) for path in missing[:3]
        )

        raise FileNotFoundError(
            f"음성 {len(missing)}개를 찾지 못했습니다. "
            f"예: {examples}"
        )

    # Tensor 변환.
    x = torch.stack(features).contiguous()
    y = torch.tensor(targets, dtype=torch.long)

    # 최종 데이터 크기 검사.
    assert x.ndim == 3
    assert x.shape[1:] == (MEL_COUNT, FRAME_COUNT)
    assert len(x) == len(y) == len(filenames)

    return x, y, filenames
