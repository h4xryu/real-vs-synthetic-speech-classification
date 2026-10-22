"""DNN/ 과 Rule-based/ 가 함께 쓰는 것. 목록 CSV 읽기, 예측 CSV 쓰기, 실행 인자, 점수 계산.

제출 규격:
    python predict.py 목록.csv 예측.csv

목록 CSV의 path 는 그 CSV가 있는 폴더를 기준으로 한 음성 위치다.
채점할 때 목록에는 label 열이 없다.
"""

import csv
import sys
from pathlib import Path

LABELS = ["original", "TTS", "voice_conversion", "sovits"]
SHORT = {"original": "orig", "TTS": "TTS", "voice_conversion": "VC", "sovits": "sovits"}
DATASET = Path(__file__).resolve().parents[1] / "dataset"


def read_list(path):
    """[(음성 경로, 파일 이름, 라벨 또는 None), ...]"""
    path = Path(path)
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    missing = [row["path"] for row in rows if not (path.parent / row["path"]).exists()]
    if missing:
        raise SystemExit(f"{path} 의 음성 {len(rows)}개 중 {len(missing)}개가 없습니다 (예: {missing[0]}).\n"
                         "데이터를 다시 받아 dataset/audio/ 를 채워 주세요.")
    return [(path.parent / row["path"], Path(row["path"]).name, row.get("label") or None) for row in rows]


def write_predictions(path, names, labels):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["filename", "pred_label"])
        writer.writerows(zip(names, labels))


def submission_paths():
    """제출 규격의 (목록 CSV, 예측 CSV). 인자 없이 실행하면 None 이고 학습(+검증)을 한다."""
    if len(sys.argv) == 1:
        return None
    if len(sys.argv) != 3:
        raise SystemExit("사용법: python predict.py 목록.csv 예측.csv")
    return sys.argv[1], sys.argv[2]


def show_valid_score(pred_csv):
    print(f"예측 파일: {pred_csv}")
    print(score_files(DATASET / "valid.csv", pred_csv))


# ---------- 점수: accuracy, macro F1, 혼동 행렬. 조교 채점도 이 계산을 쓴다.


class FormatError(Exception):
    """예측 CSV가 제출 규격과 다르다."""


def read_truth(list_csv):
    with Path(list_csv).open(encoding="utf-8", newline="") as handle:
        return {Path(row["path"]).name: row["label"] for row in csv.DictReader(handle)}


def read_predictions(pred_csv, expected_names):
    pred_csv = Path(pred_csv)
    if not pred_csv.exists():
        raise FormatError(f"예측 CSV가 만들어지지 않았습니다: {pred_csv}")
    with pred_csv.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, [])
        if header != ["filename", "pred_label"]:
            raise FormatError(f"첫 줄은 filename,pred_label 이어야 합니다. 지금: {','.join(header)}")
        pred = {}
        for line_no, row in enumerate(reader, start=2):
            if not row:
                continue
            if len(row) != 2:
                raise FormatError(f"{line_no}번째 줄의 열이 2개가 아닙니다: {row}")
            name, label = Path(row[0].strip()).name, row[1].strip()
            if label not in LABELS:
                raise FormatError(f"{line_no}번째 줄 알 수 없는 pred_label: {label!r}")
            if name in pred:
                raise FormatError(f"filename 이 두 번 나옵니다: {name}")
            pred[name] = label
    missing = sorted(set(expected_names) - set(pred))
    extra = sorted(set(pred) - set(expected_names))
    if missing or extra:
        raise FormatError(f"파일 목록이 다릅니다. 빠짐 {len(missing)} {missing[:3]} 추가 {len(extra)} {extra[:3]}")
    return pred


def compute(truth, pred):
    """truth, pred: {파일 이름: 라벨}. 점수와 혼동 행렬을 돌려준다."""
    matrix = {gold: {guess: 0 for guess in LABELS} for gold in LABELS}
    for name, gold in truth.items():
        matrix[gold][pred[name]] += 1
    per_label = {}
    for label in LABELS:
        tp = matrix[label][label]
        fp = sum(matrix[gold][label] for gold in LABELS) - tp
        fn = sum(matrix[label].values()) - tp
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        per_label[label] = {"precision": precision, "recall": recall, "f1": f1, "support": tp + fn}
    correct = sum(matrix[label][label] for label in LABELS)
    return {
        "files": len(truth),
        "accuracy": correct / len(truth),
        "macro_f1": sum(item["f1"] for item in per_label.values()) / len(LABELS),
        "per_label": per_label,
        "matrix": matrix,
    }


def format_report(result):
    lines = [
        f"{'files':<12}{result['files']}",
        f"{'accuracy':<12}{result['accuracy']:.4f}",
        f"{'macro_f1':<12}{result['macro_f1']:.4f}",
        "",
        f"{'label':<18}{'precision':>10}{'recall':>10}{'f1':>10}{'support':>10}",
    ]
    for label in LABELS:
        item = result["per_label"][label]
        lines.append(f"{label:<18}{item['precision']:10.4f}{item['recall']:10.4f}{item['f1']:10.4f}{item['support']:10d}")
    lines += ["", "confusion matrix (행: 정답, 열: 예측)", f"{'':<18}" + "".join(f"{SHORT[g]:>8}" for g in LABELS)]
    for gold in LABELS:
        lines.append(f"{gold:<18}" + "".join(f"{result['matrix'][gold][g]:8d}" for g in LABELS))
    return "\n".join(lines)


def score_files(list_csv, pred_csv):
    truth = read_truth(list_csv)
    return format_report(compute(truth, read_predictions(pred_csv, truth)))
