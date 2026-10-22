"""저장한 model_weight.pt 로 예측한다. 이 파일이 제출할 때 predict.py 가 된다.

    python examples/DNN/validation.py                      # valid 예측 + accuracy, macro F1, 혼동 행렬
    python examples/DNN/validation.py 목록.csv 예측.csv    # 예측만 (제출 규격)
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import torch

from common import DATASET, LABELS, show_valid_score, submission_paths, write_predictions
from models import SmallCNN, read_table, ResU2D_LC
WEIGHT = HERE / "model_weight.pt"                     # train.py 가 저장한 가중치
OUTPUT = HERE.parents[1] / "predictions_dnn.csv"      


def predict(list_csv, out):
    if not WEIGHT.exists():
        raise SystemExit(f"가중치가 없습니다: {WEIGHT}\n먼저 python examples/DNN/train.py 로 학습하세요.")
    model = SmallCNN()
    # model = ResU2D_LC(nOUT=4, in_ch=1, out_ch=128, mid_ch=64)
    model.load_state_dict(torch.load(WEIGHT, map_location="cpu"))
    model.eval()
    x, _, names = read_table(list_csv)
    with torch.no_grad():
        pred = model(x).argmax(dim=1).tolist()
    write_predictions(out, names, [LABELS[i] for i in pred])


def main():
    paths = submission_paths()
    if paths:
        predict(*paths)
        return
    predict(DATASET / "valid.csv", OUTPUT)
    show_valid_score(OUTPUT)


if __name__ == "__main__":
    main()
