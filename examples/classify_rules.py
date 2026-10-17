"""멜 계수를 읽어 mel_rules.py의 if/elif/else로 라벨을 적는다."""

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import mel_rules
from features import load_mono, features

ROOT = Path(__file__).resolve().parents[1]


def main():
    table = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dataset" / "valid.csv"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "predictions_rules.csv"
    rows = list(csv.DictReader(table.open(encoding="utf-8")))
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["filename", "pred_label"])
        for row in rows:
            path = table.parent / row["path"]
            label = mel_rules.predict(features(load_mono(path)))
            writer.writerow([path.name, label])
    print(out)


if __name__ == "__main__":
    main()
