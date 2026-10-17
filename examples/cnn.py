"""아주 작은 CNN. 학습 목록으로 맞춘 뒤 검증 목록의 제출 파일을 만든다."""

import csv
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
import torch.nn as nn

ROOT = Path(__file__).resolve().parents[1]
SR = 16000
SAMPLES = SR * 2
LABELS = ["original", "TTS", "voice_conversion", "sovits"]


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
    spec = torch.stft(torch.from_numpy(audio), 512, 160, 400, window, return_complex=True)
    power = spec.abs().clamp_min(1e-6).pow(2)
    pooled = torch.nn.functional.adaptive_avg_pool1d(power.transpose(0, 1).unsqueeze(0), 40)
    return torch.log(pooled.squeeze(0).transpose(0, 1))


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


def read_table(path):
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    xs, ys, names = [], [], []
    for row in rows:
        audio = load_fixed(path.parent / row["path"])
        xs.append(logmel(audio))
        names.append(Path(row["path"]).name)
        if "label" in row and row["label"]:
            ys.append(LABELS.index(row["label"]))
    x = torch.stack(xs)
    y = torch.tensor(ys) if ys else None
    return x, y, names


def main():
    train_x, train_y, _ = read_table(ROOT / "dataset" / "train.csv")
    valid_x, _, valid_names = read_table(ROOT / "dataset" / "valid.csv")
    model = SmallCNN()
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()
    model.train()
    for _ in range(30):
        opt.zero_grad()
        loss = loss_fn(model(train_x), train_y)
        loss.backward()
        opt.step()
    model.eval()
    pred = model(valid_x).argmax(dim=1).tolist()
    out = ROOT / "predictions_cnn.csv"
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["filename", "pred_label"])
        writer.writerows((name, LABELS[i]) for name, i in zip(valid_names, pred))
    print(out)


if __name__ == "__main__":
    main()
