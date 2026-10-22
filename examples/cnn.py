"""아주 작은 CNN. 학습 목록으로 맞춰 가중치를 저장하고, 저장한 가중치로 예측한다.

    python examples/cnn.py                                  # train 학습 → models/cnn.pt 저장 → valid 점수
    python examples/cnn.py --input 목록.csv --output 예측.csv  # 저장한 가중치로 예측만 (제출 규격)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
import soundfile as sf
import torch
import torch.nn as nn

from common import DATASET, LABELS, parse_args, read_list, show_valid_score, write_predictions

HERE = Path(__file__).resolve().parent
MODEL = HERE / "models" / "cnn.pt"
SR = 16000
SAMPLES = SR * 2
EPOCHS = 100


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


def read_table(list_csv):
    rows = read_list(list_csv)
    x = torch.stack([logmel(load_fixed(path)) for path, _, _ in rows])
    labels = [label for _, _, label in rows]
    y = torch.tensor([LABELS.index(label) for label in labels]) if all(labels) else None
    return x, y, [name for _, name, _ in rows]


def train():
    torch.manual_seed(0)
    train_x, train_y, _ = read_table(DATASET / "train.csv")
    model = SmallCNN()
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()
    model.train()
    for epoch in range(EPOCHS):
        opt.zero_grad()
        loss = loss_fn(model(train_x), train_y)
        loss.backward()
        opt.step()
        if (epoch + 1) % 20 == 0:
            print(f"epoch {epoch + 1:3d}  loss {loss.item():.4f}")
    MODEL.parent.mkdir(exist_ok=True)
    torch.save(model.state_dict(), MODEL)
    print(f"가중치 저장: {MODEL}")


def predict(list_csv, out):
    model = SmallCNN()
    model.load_state_dict(torch.load(MODEL, map_location="cpu"))
    model.eval()
    x, _, names = read_table(list_csv)
    with torch.no_grad():
        pred = model(x).argmax(dim=1).tolist()
    write_predictions(out, names, [LABELS[i] for i in pred])


def main():
    args = parse_args("CNN 분류")
    if args.input:
        predict(args.input, args.output)
        return
    train()
    out = Path(args.output) if args.output else HERE.parent / "predictions_cnn.csv"
    predict(DATASET / "valid.csv", out)
    show_valid_score(out)


if __name__ == "__main__":
    main()
