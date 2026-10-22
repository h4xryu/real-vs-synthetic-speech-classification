"""train.csv 로 SmallCNN 을 학습해 model_weight.pt 로 저장한다.

    python examples/DNN/train.py
    python examples/DNN/validation.py    # 저장한 가중치로 valid 점수 확인
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import torch
import torch.nn as nn

from common import DATASET
from models import SmallCNN, read_table

WEIGHT = HERE / "model_weight.pt"  # 저장할 가중치
EPOCHS = 100
LR = 1e-3
SEED = 0


def main():
    torch.manual_seed(SEED)
    x, y, _ = read_table(DATASET / "train.csv")
    model = SmallCNN()
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    loss_fn = nn.CrossEntropyLoss()
    model.train()
    for epoch in range(EPOCHS):
        print(f"epoch {epoch + 1:3d} / {EPOCHS:3d}")
        opt.zero_grad()
        out = model(x)
        loss = loss_fn(out, y)
        loss.backward()
        opt.step()
        acc = (out.argmax(dim=1) == y).float().mean().item()
        print(f"epoch {epoch + 1:3d}  loss {loss.item():.4f}  train acc {acc:.4f}")
    
    torch.save(model.state_dict(), WEIGHT)
    print(f"가중치 저장: {WEIGHT}")


if __name__ == "__main__":
    main()
