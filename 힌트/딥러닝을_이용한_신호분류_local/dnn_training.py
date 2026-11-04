"""학부용 DNN 학습과 valid 비교.

프로젝트 폴더에서 실행:
    python examples/학부용/dnn_training.py

train.csv로 학습하고 valid.csv만 평가한다.
"""

import csv
from pathlib import Path
import sys

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

# 공통 경로를 등록해 프로젝트의 기존 데이터 위치를 찾는다.
HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from models import ResU2D_LC, SmallCNN
from preprocessing import read_dataset
from utils import LABELS, classification_metrics, print_confusion_matrix, set_seed


# 학습·검증 CSV는 프로젝트의 dataset 폴더에 있다.
DATASET = PROJECT_ROOT / "dataset"
TRAIN_CSV = DATASET / "train.csv"
VALID_CSV = DATASET / "valid.csv"

# 각 설정을 직접 바꿔 작은 실험을 할 수 있다.
EPOCHS = 20
RANDOM_SEED = 0
MODEL_NAMES = ["SmallCNN", "ResU2D_LC"]
LEARNING_RATES = [0.001, 0.0005]
BATCH_SIZES = [16, 32]

# CPU만 있어도 실행되며, CUDA가 있으면 GPU를 사용한다.
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def make_model(model_name):
    """이름에 맞는 네트워크를 만든다."""
    if model_name == "SmallCNN":
        return SmallCNN(nOUT=len(LABELS))

    if model_name == "ResU2D_LC":
        return ResU2D_LC(
            nOUT=len(LABELS),
            in_ch=1,
            out_ch=128,
            mid_ch=64,
        )

    raise ValueError(f"모르는 모델 이름입니다: {model_name}")


def evaluate(model, batches, loss_function):
    """valid 데이터를 한 번 훑어 loss, accuracy, macro-F1, 혼동 행렬을 구한다."""
    model.eval()
    total_loss = 0.0
    targets = []
    predictions = []

    # 평가 단계에서는 gradient를 저장하지 않아 메모리와 시간을 줄인다.
    with torch.no_grad():
        for batch_x, batch_y in batches:
            batch_x = batch_x.to(DEVICE)
            batch_y = batch_y.to(DEVICE)

            # 모델 출력은 클래스별 점수(logits)다.
            logits = model(batch_x)
            loss = loss_function(logits, batch_y)
            total_loss += loss.item() * len(batch_y)

            # 가장 점수가 높은 클래스를 예측으로 기록한다.
            predictions.extend(logits.argmax(dim=1).cpu().tolist())
            targets.extend(batch_y.cpu().tolist())

    # 공통 함수가 accuracy, macro-F1, 혼동 행렬을 계산한다.
    metrics = classification_metrics(targets, predictions)
    metrics["loss"] = total_loss / max(len(targets), 1)
    return metrics


def train_one_setting(model_name, learning_rate, batch_size, x_train, y_train, x_valid, y_valid):
    """모델 하나를 학습하고 valid macro-F1이 가장 좋을 때의 가중치를 저장한다."""
    # 설정마다 같은 초기 난수를 사용해 비교를 조금 더 공정하게 한다.
    set_seed(RANDOM_SEED)

    model = make_model(model_name).to(DEVICE)

    # train은 섞어서 학습하고, valid는 순서를 유지해 평가한다.
    train_batches = DataLoader(
        TensorDataset(x_train, y_train),
        batch_size=batch_size,
        shuffle=True,
        num_workers=0,
    )
    valid_batches = DataLoader(
        TensorDataset(x_valid, y_valid),
        batch_size=batch_size,
        shuffle=False,
        num_workers=0,
    )

    # Adam은 신경망 가중치를 갱신하고 CrossEntropyLoss는 분류 오차를 계산한다.
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    loss_function = nn.CrossEntropyLoss()

    best_valid_f1 = -1.0
    best_epoch = 0
    best_metrics = None

    for epoch in range(1, EPOCHS + 1):
        model.train()
        train_loss = 0.0
        train_correct = 0

        # 한 epoch 동안 train 데이터를 batch 단위로 반복한다.
        for batch_x, batch_y in train_batches:
            batch_x = batch_x.to(DEVICE)
            batch_y = batch_y.to(DEVICE)

            # 이전 batch의 gradient를 지우고 현재 batch의 오차를 계산한다.
            optimizer.zero_grad()
            logits = model(batch_x)
            loss = loss_function(logits, batch_y)

            # 오차가 줄어드는 방향을 계산하고 모델 가중치를 갱신한다.
            loss.backward()
            optimizer.step()

            # epoch 전체 평균 loss와 학습 정확도를 기록한다.
            train_loss += loss.item() * len(batch_y)
            train_correct += (logits.argmax(dim=1) == batch_y).sum().item()

        # 학습에 쓰지 않는 valid 데이터로 현재 모델을 평가한다.
        valid_metrics = evaluate(model, valid_batches, loss_function)
        average_train_loss = train_loss / len(y_train)
        train_accuracy = train_correct / len(y_train)

        print(
            f"epoch {epoch:02d}/{EPOCHS} | "
            f"train loss={average_train_loss:.4f} acc={train_accuracy:.3f} | "
            f"valid loss={valid_metrics['loss']:.4f} "
            f"acc={valid_metrics['accuracy']:.3f} "
            f"macro-F1={valid_metrics['macro_f1']:.3f}"
        )

        # valid macro-F1이 가장 높은 epoch의 가중치만 남긴다.
        if valid_metrics["macro_f1"] > best_valid_f1:
            best_valid_f1 = valid_metrics["macro_f1"]
            best_epoch = epoch
            best_metrics = valid_metrics

            # 설정별 파일명으로 저장해 다른 실험 결과를 덮어쓰지 않는다.
            weight_dir = HERE / "weights"
            weight_dir.mkdir(parents=True, exist_ok=True)
            weight_path = weight_dir / (
                f"{model_name}_lr{learning_rate}_batch{batch_size}.pt"
            )
            torch.save(model.state_dict(), weight_path)

        # 이번 epoch의 valid 혼동 행렬을 확인한다.
        print_confusion_matrix(valid_metrics["confusion_matrix"])

    return {
        "model": model_name,
        "learning_rate": learning_rate,
        "batch_size": batch_size,
        "best_epoch": best_epoch,
        "valid_accuracy": best_metrics["accuracy"],
        "valid_macro_f1": best_metrics["macro_f1"],
    }


def main():
    """데이터를 읽고 사람이 읽기 쉬운 for문으로 설정들을 비교한다."""
    if not TRAIN_CSV.is_file():
        raise FileNotFoundError(f"train 목록을 찾지 못했습니다: {TRAIN_CSV}")
    if not VALID_CSV.is_file():
        raise FileNotFoundError(f"valid 목록을 찾지 못했습니다: {VALID_CSV}")

    print("사용 장치:", DEVICE)
    print("전처리 중: train.csv")
    x_train, y_train, _ = read_dataset(TRAIN_CSV)
    print("전처리 중: valid.csv")
    x_valid, y_valid, _ = read_dataset(VALID_CSV)

    print("train 입력 모양:", tuple(x_train.shape))
    print("valid 입력 모양:", tuple(x_valid.shape))
    print("클래스 순서:", LABELS)

    results = []

    # 아래 세 for문이 비교할 모델·학습률·batch size 조합을 모두 만든다.
    for model_name in MODEL_NAMES:
        for learning_rate in LEARNING_RATES:
            for batch_size in BATCH_SIZES:
                print("\n" + "=" * 70)
                print(
                    f"모델: {model_name} | 학습률: {learning_rate} "
                    f"| batch size: {batch_size}"
                )

                result = train_one_setting(
                    model_name,
                    learning_rate,
                    batch_size,
                    x_train,
                    y_train,
                    x_valid,
                    y_valid,
                )
                results.append(result)
                print(
                    f"최고 valid 결과: epoch={result['best_epoch']} "
                    f"accuracy={result['valid_accuracy']:.3f} "
                    f"macro-F1={result['valid_macro_f1']:.3f}"
                )

    # 설정별 valid 성능을 높은 macro-F1 순서로 출력하고 CSV로 저장한다.
    results.sort(key=lambda result: result["valid_macro_f1"], reverse=True)
    print("\n전체 설정 비교 (valid만 사용)")
    for result in results:
        print(
            f"{result['model']:<12} "
            f"lr={result['learning_rate']:<8} "
            f"batch={result['batch_size']:<3} "
            f"epoch={result['best_epoch']:<3} "
            f"accuracy={result['valid_accuracy']:.3f} "
            f"macro-F1={result['valid_macro_f1']:.3f}"
        )

    result_path = HERE / "valid_results.csv"
    with result_path.open("w", encoding="utf-8", newline="") as file:
        fieldnames = [
            "model",
            "learning_rate",
            "batch_size",
            "best_epoch",
            "valid_accuracy",
            "valid_macro_f1",
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nvalid 결과 저장: {result_path}")
    print(f"최고 가중치 저장 폴더: {HERE / 'weights'}")


if __name__ == "__main__":
    main()
