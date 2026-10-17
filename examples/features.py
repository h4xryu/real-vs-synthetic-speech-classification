"""멜 필터와 간단한 청각 특징. 분류 규칙은 여기 두지 않는다."""

import math

import numpy as np
import soundfile as sf

N_MELS = 26
SR = 16000
WIN = 400
HOP = 160


def load_mono(path):
    audio, sr = sf.read(path, always_2d=False)
    audio = np.asarray(audio, dtype=np.float32)
    if audio.ndim > 1:
        audio = audio.mean(axis=1)
    if sr != SR:
        n = int(round(len(audio) * SR / sr))
        audio = np.interp(np.linspace(0, len(audio), n, endpoint=False), np.arange(len(audio)), audio).astype(np.float32)
    return audio


def _hz_to_mel(hz):
    return 2595.0 * math.log10(1.0 + hz / 700.0)


def _mel_to_hz(mel):
    return 700.0 * (10.0 ** (mel / 2595.0) - 1.0)


def _mel_filters():
    n_freq = WIN // 2 + 1
    low, high = _hz_to_mel(0.0), _hz_to_mel(SR / 2)
    points = [_mel_to_hz(low + i * (high - low) / (N_MELS + 1)) for i in range(N_MELS + 2)]
    bins = [min(n_freq - 1, int((WIN + 1) * point / SR)) for point in points]
    weights = np.zeros((N_MELS, n_freq), dtype=np.float32)
    for i in range(N_MELS):
        left, center, right = bins[i], bins[i + 1], bins[i + 2]
        if center == left:
            center += 1
        if right == center:
            right += 1
        for k in range(left, center):
            weights[i, k] = (k - left) / (center - left)
        for k in range(center, min(right, n_freq)):
            weights[i, k] = (right - k) / (right - center)
    return weights


FILTERS = _mel_filters()
WINDOW = np.hanning(WIN).astype(np.float32)


def features(audio):
    if len(audio) < WIN:
        audio = np.pad(audio, (0, WIN - len(audio)))
    frames = 1 + (len(audio) - WIN) // HOP
    mels = []
    centroids = []
    flatness = []
    rolloffs = []
    for i in range(frames):
        chunk = audio[i * HOP:i * HOP + WIN] * WINDOW
        spec = np.abs(np.fft.rfft(chunk)) ** 2
        mel = FILTERS @ spec + 1e-10
        mels.append(np.log(mel))
        freqs = np.linspace(0, SR / 2, len(spec))
        power = spec.sum() + 1e-10
        centroids.append((freqs * spec).sum() / power)
        flatness.append(math.exp(np.log(spec + 1e-10).mean()) / (spec.mean() + 1e-10))
        cumulative = np.cumsum(spec)
        rolloffs.append(freqs[min(len(freqs) - 1, int(np.searchsorted(cumulative, 0.85 * cumulative[-1])))])
    mel_mean = np.mean(mels, axis=0)
    total = float(np.exp(mel_mean).sum()) + 1e-10
    rms = math.sqrt(float(np.mean(audio ** 2)) + 1e-12)
    signs = np.sign(audio)
    zcr = float(np.mean(np.abs(np.diff(signs)))) / 2
    values = list(mel_mean) + [
        float(np.mean(centroids) / 1000.0),
        float(np.mean(flatness)),
        20.0 * math.log10(rms),
        zcr,
        float(np.mean(rolloffs) / 1000.0),
        float(np.exp(mel_mean[:8]).sum() / total),
        float(np.exp(mel_mean[18:]).sum() / total),
    ]
    return [round(v, 4) for v in values]
