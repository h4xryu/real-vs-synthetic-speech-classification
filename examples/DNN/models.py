"""DNN 예시의 입력 만들기와 모델 구조. train.py 와 validation.py 가 함께 쓴다.

음성 2초 → 로그 멜 스펙트로그램 [40 멜 대역, 200 프레임] → 작은 1D CNN → 라벨 4개 점수
"""

import numpy as np
import soundfile as sf
import torch
import torch.nn as nn

from common import LABELS, read_list

# =========================================
# 전처리 부분
# =========================================

SR = 16000
SAMPLES = SR * 2
N_FFT = 512
N_MELS = 40


def mel_filterbank(n_mels=N_MELS, n_fft=N_FFT, sr=SR):
    # HTK mel 스케일 삼각 필터 [n_mels, n_fft//2+1]
    hz2mel = lambda f: 2595.0 * np.log10(1.0 + f / 700.0)
    mel2hz = lambda m: 700.0 * (10.0 ** (m / 2595.0) - 1.0)
    edges = mel2hz(np.linspace(hz2mel(0.0), hz2mel(sr / 2), n_mels + 2))
    freqs = np.linspace(0.0, sr / 2, n_fft // 2 + 1)
    lo, mid, hi = edges[:-2, None], edges[1:-1, None], edges[2:, None]
    fb = np.maximum(0.0, np.minimum((freqs - lo) / (mid - lo), (hi - freqs) / (hi - mid)))
    return torch.tensor(fb, dtype=torch.float32)


MEL_FB = mel_filterbank()


def load_fixed(path):
    audio, sr = sf.read(path, always_2d=False)
    audio = np.asarray(audio, dtype=np.float32)
    if audio.ndim > 1:
        audio = audio.mean(axis=1)
    if sr != SR:
        n = int(round(len(audio) * SR / sr))
        audio = np.interp(np.linspace(0, len(audio), n, endpoint=False), np.arange(len(audio)), audio)
    audio = audio.astype(np.float32)
    if len(audio) < SAMPLES:
        audio = np.pad(audio, (0, SAMPLES - len(audio)))
    return audio[:SAMPLES]


def logmel(audio):
    window = torch.hann_window(400)
    spec = torch.stft(torch.from_numpy(audio), 512, 160, 400, window, return_complex=True)[:, :SAMPLES // 160]
    power = spec.abs().pow(2)
    return torch.log((MEL_FB @ power).clamp_min(1e-6))


def read_table(list_csv):
    rows = read_list(list_csv)
    x = torch.stack([logmel(load_fixed(path)) for path, _, _ in rows])
    labels = [label for _, _, label in rows]
    y = torch.tensor([LABELS.index(label) for label in labels]) if all(labels) else None
    return x, y, [name for _, name, _ in rows]

# =========================================
# Model 구조 (주로 변경)
# =========================================

class SmallCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv1d(40, 16, 5, padding=2),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(16, 16, 5, padding=2),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1),
        )
        self.fc = nn.Linear(16, len(LABELS))

    def forward(self, x):
        return self.fc(self.net(x).squeeze(-1))







































