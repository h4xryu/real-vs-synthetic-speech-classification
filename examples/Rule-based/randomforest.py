"""랜덤 포레스트 학습. features.py 의 특징 47개로 if/else 나무를 여러 그루 자동으로 만들어 randomforest.joblib 로 저장한다.

    python examples/Rule-based/randomforest.py
    python examples/Rule-based/validation.py    # METHOD = "randomforest" 로 바꾸고 valid 점수 확인
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import joblib
from sklearn.ensemble import RandomForestClassifier

from common import DATASET
from features import feature_table

WEIGHT = HERE / "randomforest.joblib"  # 저장할 가중치
N_TREES = 300
SEED = 0


def main():
    x, y, _ = feature_table(DATASET / "train.csv")
    model = RandomForestClassifier(n_estimators=N_TREES, random_state=SEED)
    model.fit(x, y)
    print(f"train acc {model.score(x, y):.4f}")
    joblib.dump(model, WEIGHT)
    print(f"가중치 저장: {WEIGHT}")
    top = sorted(enumerate(model.feature_importances_), key=lambda item: -item[1])[:5]
    print("중요한 특징 c[i]:", ", ".join(f"c[{i}] {w:.3f}" for i, w in top))


if __name__ == "__main__":
    main()
