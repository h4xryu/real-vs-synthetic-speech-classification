#!/usr/bin/env python3
"""비공개 테스트 정답과 제출 CSV를 맞춰 macro F1을 출력한다.

제출 파일 헤더:
    filename,pred_label

pred_label 은 original, TTS, voice_conversion, sovits 중 하나다.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

LABELS = ("original", "TTS", "voice_conversion", "sovits")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def f1(precision: float, recall: float) -> float:
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def main() -> None:
    parser = argparse.ArgumentParser(description="4-class submission scorer")
    parser.add_argument("--pred", required=True, help="filename,pred_label CSV")
    parser.add_argument("--truth", required=True, help="private test.csv")
    args = parser.parse_args()

    with Path(args.pred).open(encoding="utf-8", newline="") as handle:
        header = next(csv.reader(handle), [])
    if header != ["filename", "pred_label"]:
        raise SystemExit("제출 CSV 헤더는 filename,pred_label 이어야 합니다.")
    truth_rows = read_csv(Path(args.truth))
    pred_rows = read_csv(Path(args.pred))

    truth = {}
    for row in truth_rows:
        name = Path(row["path"]).name
        truth[name] = row["label"]
    pred = {}
    for row in pred_rows:
        name = Path(row["filename"]).name
        label = row["pred_label"].strip()
        if label not in LABELS:
            raise SystemExit(f"알 수 없는 pred_label: {label}")
        if name in pred:
            raise SystemExit(f"filename 이 두 번 나옵니다: {name}")
        pred[name] = label

    missing = sorted(set(truth) - set(pred))
    extra = sorted(set(pred) - set(truth))
    if missing or extra:
        raise SystemExit(f"파일 수가 정답과 다릅니다. 빠짐 {len(missing)} 추가 {len(extra)}")

    correct = 0
    counts = {label: {"tp": 0, "fp": 0, "fn": 0, "support": 0} for label in LABELS}
    for name, gold in truth.items():
        guess = pred[name]
        counts[gold]["support"] += 1
        if guess == gold:
            correct += 1
            counts[gold]["tp"] += 1
        else:
            counts[gold]["fn"] += 1
            counts[guess]["fp"] += 1

    print(f"{'files':<16}{len(truth)}")
    print(f"{'accuracy':<16}{correct / len(truth):.4f}")
    macros = []
    print()
    print(f"{'label':<18}{'precision':>10}{'recall':>10}{'f1':>10}{'support':>10}")
    for label in LABELS:
        item = counts[label]
        precision = item["tp"] / (item["tp"] + item["fp"]) if item["tp"] + item["fp"] else 0.0
        recall = item["tp"] / (item["tp"] + item["fn"]) if item["tp"] + item["fn"] else 0.0
        score = f1(precision, recall)
        macros.append(score)
        print(f"{label:<18}{precision:10.4f}{recall:10.4f}{score:10.4f}{item['support']:10d}")
    print()
    print(f"{'macro_f1':<16}{sum(macros) / len(macros):.4f}")


if __name__ == "__main__":
    main()
