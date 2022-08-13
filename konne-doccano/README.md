konne-doccano

# 한국어 중첩 개체명 말뭉치 주석 작업

konec v1.0.0을 doccano에서 작업 가능한 형식으로 변환하고 중첩 개체명 주석.

## doccano

- doccano: https://github.com/doccano/doccano
- doccano의 Sequence Labeling (Named Entity) 주석 프로젝트 이용
  - Allow overlapping entity 옵션 이용. 중첩 태깅 허용.

### 데이터셋 파일 형식

- JSONL
- 필수 요소: text (원문), label(주석)
- 주석: `[begin, end, label]`의 배열
- 기타 요소 자유롭게 추가 가능

```jsonl
{"klue_id": "klue-ner-v1_dev_04986-nsmc", "text": "베니니영화에 따라다니는 니콜레타의 매력을 제대로 볼수있는영화,", "label": [[0, 3, "PS_NAME"], [13, 17, "PS_NAME"]]}
```

### 라벨 정보 파일

- [doccano-label-config.json](doccano-label-config.json)


```json
[
  {
    "id" : 1,
	"text" : "PS_NAME",
	"backgroundColor" : "#ff0000",
	"textColor" : "#ffffff",
	"prefixKey" : null,
	"suffixKey" : null
  },
  {
    "id" : 2,
	"text" : "PS_CHARACTER",
	"backgroundColor" : "#ff0000",
	"textColor" : "#ffffff",
	"prefixKey" : null,
	"suffixKey" : null
  }
]
```


Label color


```
PS 18449 (red) #9f0500
CV 14056 (dark blue) #0062B1
OG 10874 (orange) #F44E3B
LC  9055 (yellow) #FCDC00
AF  5034 (violet) #7B64FF
TM  3180 (black) #000000
EV  1774 (purple) #AB149E
QT 14056 (dark green) #194D33
DT 10312 (medium green) #68BC00
TI  2616 (ligt green) #A4DD00
AM  1268 (gray) #333333
MT   161
PT   113
TR   200
FD   140
```

