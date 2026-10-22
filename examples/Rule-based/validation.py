"""특징 47개를 뽑아 METHOD 로 고른 분류기로 예측한다. 이 파일이 제출할 때 predict.py 가 된다.

    python examples/Rule-based/validation.py                      # valid 예측 + accuracy, macro F1, 혼동 행렬
    python examples/Rule-based/validation.py 목록.csv 예측.csv    # 예측만 (제출 규격)

METHOD
    "ifelse"        rules/ifelse.py 의 if/elif/else. 학습 없음
    "randomforest"  randomforest.py 로 학습한 randomforest.joblib
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

from common import DATASET, show_valid_score, submission_paths, write_predictions
from features import feature_table

METHOD = "randomforest"                                         # "ifelse", "randomforest"
OUTPUT = HERE.parents[1] / f"predictions_{METHOD}.csv"   


def classify(x):
    if METHOD == "ifelse":
        from rules import ifelse

        return [ifelse.predict(list(row)) for row in x]
    import joblib

    weight = HERE / f"{METHOD}.joblib"
    if not weight.exists():
        raise SystemExit(f"가중치가 없습니다: {weight}\n먼저 python examples/Rule-based/{METHOD}.py 로 학습하세요.")
    return list(joblib.load(weight).predict(x))


def predict(list_csv, out):
    x, _, names = feature_table(list_csv)
    write_predictions(out, names, classify(x))


def main():
    paths = submission_paths()
    if paths:
        predict(*paths)
        return
    print(f"METHOD = {METHOD}")
    predict(DATASET / "valid.csv", OUTPUT)
    show_valid_score(OUTPUT)


if __name__ == "__main__":
    main()
