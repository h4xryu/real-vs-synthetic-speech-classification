

import csv
from pathlib import Path
import sys

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from models import ResU2D_LC
from preprocessing import read_dataset
from utils import LABELS, classification_metrics, print_confusion_matrix, set_seed


DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def evaluate(model, loader):
    model.eval()
    loss_fn = nn.CrossEntropyLoss()

    total_loss = 0
    targets, predictions = [], []

    with torch.no_grad():
        for x, y in loader:
            x, y = x.to(DEVICE), y.to(DEVICE)

            logits = model(x)
            total_loss += loss_fn(logits, y).item() * len(y)

            predictions.extend(logits.argmax(1).cpu().tolist())
            targets.extend(y.cpu().tolist())

    metrics = classification_metrics(targets, predictions)
    metrics["loss"] = total_loss / len(targets)

    return metrics


def main():
    x_train, y_train, _ = read_dataset(PROJECT_ROOT / "dataset/train.csv")
    x_valid, y_valid, _ = read_dataset(PROJECT_ROOT / "dataset/valid.csv")

    print("Device:", DEVICE)
    print("Train:", x_train.shape)
    print("Valid:", x_valid.shape)
    print("Classes:", LABELS)

    results = []

    # 실험 설정
    for model_name in ["ResU2D_LC"]:
        for mid_ch in [64, 32, 8]:
            for out_ch in [128, 64, 32]:
                for lr in [0.001, 0.0005]:
                    for batch_size in [16, 32]:
                        for seed in [0, 42, 123]:
                            for scheduler_name in ["none", "step", "cosine"]:

                    

                                print("\n" + "=" * 70)
                                print(
                                    f"{model_name} | mid={mid_ch} | out={out_ch} "
                                    f"| lr={lr} | batch={batch_size} "
                                    f"| seed={seed} | scheduler={scheduler_name}"
                                )

                                set_seed(seed)

                                # 모델 생성
                                model = ResU2D_LC(
                                        nOUT=len(LABELS),
                                        in_ch=1,
                                        mid_ch=mid_ch,
                                        out_ch=out_ch,
                                    )
                                    

                                model = model.to(DEVICE)

                                train_loader = DataLoader(
                                    TensorDataset(x_train, y_train),
                                    batch_size=batch_size,
                                    shuffle=True,
                                    num_workers=0,
                                )

                                valid_loader = DataLoader(
                                    TensorDataset(x_valid, y_valid),
                                    batch_size=batch_size,
                                    shuffle=False,
                                    num_workers=0,
                                )

                                optimizer = torch.optim.Adam(
                                    model.parameters(), lr=lr
                                )
                                loss_fn = nn.CrossEntropyLoss()

                                # 학습률 스케줄러
                                if scheduler_name == "step":
                                    scheduler = torch.optim.lr_scheduler.StepLR(
                                        optimizer, step_size=5, gamma=0.5
                                    )
                                elif scheduler_name == "cosine":
                                    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                                        optimizer, T_max=20
                                    )
                                else:
                                    scheduler = None

                                best_f1 = -1
                                best_epoch = 0
                                best_metrics = None

                                for epoch in range(1, 21):
                                    model.train()
                                    total_loss = 0
                                    correct = 0

                                    for x, y in train_loader:
                                        x, y = x.to(DEVICE), y.to(DEVICE)

                                        optimizer.zero_grad()
                                        logits = model(x)
                                        loss = loss_fn(logits, y)

                                        loss.backward()
                                        optimizer.step()

                                        total_loss += loss.item() * len(y)
                                        correct += (logits.argmax(1) == y).sum().item()

                                    if scheduler is not None:
                                        scheduler.step()

                                    train_loss = total_loss / len(y_train)
                                    train_acc = correct / len(y_train)

                                    valid = evaluate(model, valid_loader)

                                    print(
                                        f"Epoch {epoch:02d}/20 | "
                                        f"Train Loss={train_loss:.4f} "
                                        f"Acc={train_acc:.3f} | "
                                        f"Valid Loss={valid['loss']:.4f} "
                                        f"Acc={valid['accuracy']:.3f} "
                                        f"F1={valid['macro_f1']:.3f}"
                                    )

                                    if valid["macro_f1"] > best_f1:
                                        best_f1 = valid["macro_f1"]
                                        best_epoch = epoch
                                        best_metrics = valid

                                        weight_dir = HERE / "weights"
                                        weight_dir.mkdir(exist_ok=True)

                                        torch.save(
                                            model.state_dict(),
                                            weight_dir / (
                                                f"{model_name}_mid{mid_ch}_out{out_ch}"
                                                f"_lr{lr}_bs{batch_size}"
                                                f"_seed{seed}_{scheduler_name}.pt"
                                            ),
                                        )

                                    print_confusion_matrix(
                                        valid["confusion_matrix"]
                                    )

                                results.append({
                                    "model": model_name,
                                    "mid_ch": mid_ch,
                                    "out_ch": out_ch,
                                    "lr": lr,
                                    "batch_size": batch_size,
                                    "seed": seed,
                                    "scheduler": scheduler_name,
                                    "best_epoch": best_epoch,
                                    "valid_accuracy": best_metrics["accuracy"],
                                    "valid_macro_f1": best_metrics["macro_f1"],
                                })

    # valid macro-F1 기준 정렬
    results.sort(
        key=lambda x: x["valid_macro_f1"],
        reverse=True,
    )

    print("\n전체 실험 결과")
    for r in results:
        print(
            f"{r['model']:<12} "
            f"mid={r['mid_ch']:<3} "
            f"out={r['out_ch']:<3} "
            f"lr={r['lr']:<8} "
            f"batch={r['batch_size']:<3} "
            f"seed={r['seed']:<3} "
            f"scheduler={r['scheduler']:<7} "
            f"epoch={r['best_epoch']:<3} "
            f"acc={r['valid_accuracy']:.3f} "
            f"F1={r['valid_macro_f1']:.3f}"
        )

    with open(HERE / "valid_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print("\n결과 저장:", HERE / "valid_results.csv")


if __name__ == "__main__":
    main()
