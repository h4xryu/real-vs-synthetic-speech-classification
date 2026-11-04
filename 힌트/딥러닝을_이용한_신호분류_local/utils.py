"""학부 실습에서 반복해서 쓰는 작은 학습·평가 함수."""

import random

import numpy as np
import torch


# 숫자 라벨과 CSV의 문자열 라벨은 이 순서로 연결된다.
LABELS = ["original", "TTS", "voice_conversion", "sovits"]


def set_seed(seed):
    """같은 설정으로 다시 실행할 때 결과가 비슷하도록 난수를 고정한다."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def classification_metrics(targets, predictions):
    """정답과 예측으로 accuracy, macro-F1, confusion matrix를 계산한다."""
    targets = np.asarray(targets, dtype=np.int64)
    predictions = np.asarray(predictions, dtype=np.int64)
    class_count = len(LABELS)

    # 행은 실제 라벨, 열은 모델 예측 라벨이다.
    matrix = np.zeros((class_count, class_count), dtype=np.int64)
    for target, prediction in zip(targets, predictions):
        matrix[target, prediction] += 1

    # Accuracy는 전체 음성 중 맞힌 음성의 비율이다.
    accuracy = float(np.trace(matrix) / max(len(targets), 1))

    # Macro-F1은 클래스마다 F1을 구해 같은 비중으로 평균낸다.
    class_f1 = []
    for class_index in range(class_count):
        true_positive = matrix[class_index, class_index]
        false_positive = matrix[:, class_index].sum() - true_positive
        false_negative = matrix[class_index, :].sum() - true_positive

        precision = true_positive / max(true_positive + false_positive, 1)
        recall = true_positive / max(true_positive + false_negative, 1)
        f1 = 2 * precision * recall / max(precision + recall, 1e-12)
        class_f1.append(f1)

    return {
        "accuracy": accuracy,
        "macro_f1": float(np.mean(class_f1)),
        "confusion_matrix": matrix,
    }


def print_confusion_matrix(matrix):
    """실제 라벨(행)과 예측 라벨(열)을 읽기 쉬운 표로 출력한다."""
    label_width = max(len(label) for label in LABELS) + 2
    print("행=실제 라벨, 열=예측 라벨")
    print(" " * label_width + "".join(f"{label:>{label_width}}" for label in LABELS))
    for label, row in zip(LABELS, matrix):
        values = "".join(f"{int(value):>{label_width}d}" for value in row)
        print(f"{label:<{label_width}}{values}")
