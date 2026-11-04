# 학부용 DNN 음성 분류

W&B 없이 `train.csv`로 학습하고 `valid.csv` 성능만 비교하는 간단한 예제입니다.
별도 설정 파일이나 명령행 옵션 없이 for문에 적힌 설정들을 순서대로 실행합니다.

## 실행

프로젝트 최상위 폴더에서:

```powershell
python examples/학부용/dnn_training.py
```

필요한 Python 패키지는 프로젝트 `requirements.txt`에 있습니다.

## 파일

- `preprocessing.py`: 음성을 mono 16 kHz, 2초로 맞추고 `[40, 200]` 로그멜 특징으로 변환합니다.
- `models.py`: 간단한 `SmallCNN`과 프로젝트 입력에 맞춘 `ResU2D_LC`를 정의합니다.
- `utils.py`: 난수 고정, accuracy/macro-F1, 혼동 행렬 출력을 담당합니다.
- `dnn_training.py`: 학습·valid 평가·설정 비교를 순서대로 수행합니다.

## 설정 바꾸기

`dnn_training.py` 상단의 다음 리스트를 수정하면 비교할 조합을 바꿀 수 있습니다.

```python
MODEL_NAMES = ["SmallCNN", "ResU2D_LC"]
LEARNING_RATES = [0.001, 0.0005]
BATCH_SIZES = [16, 32]
```

예를 들어 SmallCNN만 실행하려면 `MODEL_NAMES = ["SmallCNN"]`으로 바꿉니다.
리스트 항목의 모든 조합이 세 개의 간단한 for문으로 실행됩니다.

가장 좋은 valid macro-F1의 가중치는 `weights/`에 저장되고,
설정별 결과는 `valid_results.csv`에 저장됩니다.
