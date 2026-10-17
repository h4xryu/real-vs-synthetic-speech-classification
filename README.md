# Real vs Synthetic Speech Classification

음성 파일을 듣고, **사람이 실제로 녹음한 목소리**인지 **프로그램이 만든 목소리**인지 맞히는 과제입니다.

모델을 새로 만들어도 되고, 이미 있는 머신러닝이나 딥러닝 코드를 고쳐 써도 됩니다. 사용 언어와 라이브러리는 자유입니다. 마지막에 내는 파일 형식만 아래와 같으면 됩니다.

## 맞혀야 하는 것

정답은 네 가지 중 하나입니다. 철자가 다르면 오답입니다.

| 적을 말 | 뜻 |
|---|---|
| `original` | 사람이 실제로 녹음한 목소리 |
| `TTS` | 글자를 음성으로 읽어 만든 목소리 |
| `voice_conversion` | 다른 사람 목소리를 이 화자처럼 바꿔 만든 목소리 |
| `sovits` | 그 화자 목소리로 짧게 학습한 뒤 만든 목소리 |

`TTS`만 대문자입니다. 나머지는 소문자입니다.

`speaker_id`는 누구의 목소리인지만 알려 줍니다. 정답이 아닙니다. 같은 사람의 실제 녹음과 만든 목소리가 함께 들어 있습니다. 문장 내용은 파일마다 다릅니다. 문장이 아니라 **목소리가 어떻게 만들어졌는지**를 맞히면 됩니다.

## 받은 파일

```text
dataset/
  train.csv          학습용 목록. 정답이 적혀 있습니다.
  valid.csv          검증용 목록. 정답이 적혀 있습니다.
  audio/             위 목록의 음성 파일
submission_format.csv  내는 파일의 예시
```

테스트 음성은 이 저장소에 없습니다. 학습이 끝난 뒤 따로 받을 파일입니다. 그 파일에는 정답 열이 없습니다.

개수는 다음과 같습니다.

| 파일 | 개수 | 정답 |
|---|---|---|
| train | 16 | 있음 |
| valid | 16 | 있음 |
| test | 16 | 없음. 나중에 받습니다. |

학습, 검증 모두 화자 4명과 라벨 4개가 각각 4개씩 들어 있습니다.

## CSV 읽는 법

엑셀, 메모장, 파이썬 모두 가능합니다. 엑셀에서 한글이 깨지면 데이터 탭의 텍스트/CSV에서 원본 파일을 **UTF-8**로 여세요.

`train.csv`와 `valid.csv`의 열은 같습니다.

| 열 이름 | 예시 | 설명 |
|---|---|---|
| `path` | `audio/tr_0001.flac` | `dataset` 폴더 안에서 음성 파일의 위치 |
| `label` | `TTS` | 정답 |
| `speaker_id` | `LA_0079` | 화자 번호 |
| `sampling_rate` | `16000` | 1초에 16000번 샘플링된 소리 |
| `duration_sec` | `5.890` | 길이(초) |

음성은 모두 16 kHz, 모노, FLAC입니다. 길이는 파일마다 다릅니다.

파이썬으로 첫 줄을 확인하는 예입니다.

```python
import pandas as pd

train = pd.read_csv("dataset/train.csv")
print(train.head())
print(train["label"].value_counts())
```

`pandas`가 없으면 터미널에서 `pip install pandas`를 한 번 실행합니다.

음성 하나를 들으려면 `dataset/audio/tr_0001.flac`를 그대로 재생하면 됩니다.

## 학습과 검증

- **train**: 모델을 만들 때 사용합니다.
- **valid**: 만든 모델이 새 음성에도 맞는지 확인할 때 사용합니다. 여기 점수를 보고 모델을 고칩니다.
- **test**: 마지막에 한 번만 맞힙니다. 정답을 보면서 모델을 고치면 안 됩니다.

검증에서 잘 맞았다고 테스트에서도 같지는 않습니다. 검증 점수는 내 점검용입니다.

## 제출할 예측 코드와 입출력 규격

학생이 제출할 것은 **직접 작성한 예측 코드**입니다. `if / else` 규칙, 머신러닝, CNN·DNN 등 방법은 자유입니다. 예시 코드를 그대로 제출하는 것이 아니라, 자기 코드가 아래 입력을 읽고 지정된 출력 CSV를 만들도록 작성하면 됩니다.

예측 코드는 `train.csv`의 정답 라벨과 음성으로 학습·규칙 설정을 할 수 있고, 라벨이 없는 `test.csv`의 각 음성에 대해 하나의 라벨을 예측합니다. 음성 경로는 목록 CSV가 있는 폴더를 기준으로 찾습니다. 검증할 때는 `test.csv` 대신 `valid.csv`를 넣어 같은 흐름을 확인합니다.

예시 코드처럼 입력 목록을 읽어 각 파일을 예측하고, 결과를 CSV로 저장하면 됩니다. 예측 방법이나 내부 함수의 모양은 자유지만, **입력 파일 목록과 출력 형식은 예시 및 채점기와 같아야** 합니다.

출력 CSV의 파일 이름은 자유입니다. 첫 줄은 반드시 아래 두 열입니다.

```csv
filename,pred_label
te_0001.flac,original
te_0002.flac,TTS
```

테스트 음성 하나마다 행을 하나씩 출력합니다. `filename`은 입력 목록의 `path`에서 파일 이름만 적고, `pred_label`은 예측한 라벨을 적습니다. 이 CSV는 예측 코드가 실행 중 생성하는 결과물이며, 학생이 손으로 정답을 채워 제출하는 파일이 아닙니다.

| 열 이름 | 설명 |
|---|---|
| `filename` | 음성 파일 이름만. 폴더 경로 없이 `te_0001.flac` |
| `pred_label` | 모델이 맞힌 라벨. 위 표의 네 단어 중 하나 |

예시 파일은 `submission_format.csv`입니다. 이 파일은 출력 형식만 보여 주는 예시입니다.

확인할 것:

- 첫 줄이 `filename,pred_label` 인가
- `pred_label` 철자가 정확한가
- 테스트 파일을 빠뜨리거나 두 번 적지 않았는가
- 쉼표로 열이 나뉘는가. 엑셀에서 저장할 때 **CSV UTF-8**로 저장하세요

아래처럼 출력하면 채점되지 않습니다.

```csv
filename,label
te_0001.flac,Original
```

열 이름이 `label`이면 안 되고, `Original`처럼 대문자를 바꾸면 안 됩니다.

## 점수

채점 기준은 **macro F1**입니다.

쉽게 말하면, 네 라벨을 각각 얼마나 맞혔는지 본 다음 그 넷의 평균입니다. 한 라벨만 잘 맞히고 나머지는 틀리면 점수가 낮아집니다. 그래서 네 종류를 고루 맞히는 편이 유리합니다.

같이 나오는 accuracy는 16개 중 몇 개를 맞혔는지입니다. 순위는 accuracy가 아니라 macro F1입니다.

채점은 테스트 정답을 가진 사람이 합니다.

```bash
python3 score.py --pred 제출파일.csv --truth private/test.csv
```

학생 저장소에는 `private/test.csv`가 없습니다.

## 예시 예측 코드

두 예시는 각자 다른 방식으로 분류하지만, 모두 입력 음성 목록을 읽고 `filename,pred_label` 형식의 CSV를 만듭니다. 자기 코드를 만들 때도 이 입출력 규격을 맞추면 됩니다.

규칙 기반 예시는 멜 에너지, 스펙트럼 중심, 평탄도, RMS, 영교차율 같은 값을 뽑은 뒤 `if / elif / else`로 라벨을 고릅니다. 규칙은 `examples/mel_rules.py`에 있고, 목록을 읽어 예측 CSV를 쓰는 실행 코드는 `examples/classify_rules.py`입니다.

작은 CNN 예시는 학습 목록으로 모델을 맞춘 뒤 검증 음성의 예측 CSV를 만듭니다. 어느 방법이든 CSV의 열 이름과 라벨 표기는 동일해야 합니다.

```bash
pip install numpy soundfile
python3 examples/classify_rules.py
```

결과 파일은 `predictions_rules.csv`입니다.

작은 CNN 예는 아래입니다. 학습 16개로 잠깐 맞춘 뒤 검증 16개의 예측을 적습니다.

```bash
pip install torch soundfile
python3 examples/cnn.py
```

결과 파일은 `predictions_cnn.csv`입니다. 첫 줄은 둘 다 `filename,pred_label`입니다.
