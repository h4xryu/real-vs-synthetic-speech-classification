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

## 내는 파일

파일 이름은 자유입니다. 내용은 CSV이고, 첫 줄은 반드시 아래 두 단어입니다.

```csv
filename,pred_label
te_0001.flac,original
te_0002.flac,TTS
```

| 열 이름 | 설명 |
|---|---|
| `filename` | 음성 파일 이름만. 폴더 경로 없이 `te_0001.flac` |
| `pred_label` | 모델이 맞힌 라벨. 위 표의 네 단어 중 하나 |

예시 파일은 `submission_format.csv`입니다. 이 파일은 형식만 보여 주는 것이라 제출용이 아닙니다.

확인할 것:

- 첫 줄이 `filename,pred_label` 인가
- `pred_label` 철자가 정확한가
- 테스트 파일을 빠뜨리거나 두 번 적지 않았는가
- 쉼표로 열이 나뉘는가. 엑셀에서 저장할 때 **CSV UTF-8**로 저장하세요

아래처럼 내면 채점되지 않습니다.

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

## 예시 두 개

둘 다 검증 목록을 읽고, 같은 형식의 CSV를 만듭니다. 점수가 높지 않아도 됩니다. 내는 파일 모양만 같으면 됩니다.

규칙을 쓰는 예는 멜 에너지, 스펙트럼 중심, 평탄도, RMS, 영교차율처럼 듣는 감각에 쓰는 숫자를 뽑습니다. 그다음 `examples/mel_rules.py` 안에서 그 숫자가 얼마 이상인지, 얼마 이하인지만 봅니다. 그 파일은 `if / elif / else`만 아주 길게 있습니다. 실행은 짧은 쪽만 하면 됩니다.

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
