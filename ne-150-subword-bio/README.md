ne-150-subword-bio

# 개체명 150 부류 자동 태깅 결과

- klue-ner-v1.1의 원문을 그대로 가져와 150개 부류 개체명 태그를 자동으로 부착함.
- dev 5000문장, train 21008문장. 


## 형식

- 문장 라인은 klue-ner-v1.1과 동일
- BIO 라인은 subword 단위. 150개 부류 
- BIO 라인이 `##`으로 시작하는 경우 앞 subword와 한 어절을 이룸

```
## klue-ner-v1_train_00000_wikitree	특히 <영동고속도로:LC> <강릉:LC> 방향 <문막휴게소:LC>에서 <만종분기점:LC>까지 <5km:QT> 구간에는 승용차 전용 임시 갓길차로제를 운영하기로 했다.
특히	O
영동고속도로	B-AF_ROAD
강릉	B-LCP_CITY
방향	O
문	B-LC_OTHERS
##막	I-LC_OTHERS
##휴	I-LC_OTHERS
##게	I-LC_OTHERS
##소	I-LC_OTHERS
##에서	O
만	B-LC_OTHERS
##종	I-LC_OTHERS
```

- 문장 부호인 경우 띄어쓰기 정보를 알 수 없음
- `[UNK]`로 원문이 대치된 경우도 존재함


```
## klue-ner-v1_train_00009_nsmc 다만 너무 <김우빈:PS>의 분량만 많아서 ...ᄒ저는 <이현우:PS>팬이라 ᄒᄒᄒ그래도 재미있었어요
다만    O
너무    O
김우    B-PS_NAME
##빈    I-PS_NAME
##의    O
분량    O
##만    O
많      O
##아    O
##서    O
.       O
.       O
.       O
[UNK]   O
이현    B-PS_NAME
##우    I-PS_NAME
##팬    O
##이    O
##라    O
[UNK]   O
재미있  O
##었    O
##어요  O
```

- 연달은 subword가 B로 태깅이 된 오류가 존재함

```
## klue-ner-v1_train_00010_wikitree     <중국 후난(湖南)성 창샤(長沙)시 우자링(五家岭)가:
LC> 한 시장에서 <14일:DT> <오전 10시 15분:TI>께 칼부림 사건이 일어나 <5명:QT>이 숨지고 <1
명:QT>이 부상했다고 <중신넷:OG>이 <14일:DT> 보도했다.
중국    B-LCP_COUNTRY
후      B-LCP_PROVINCE
##난    B-LCP_PROVINCE
(       B-LCP_PROVINCE
[UNK]   B-LCP_PROVINCE
南      B-LCP_PROVINCE
)       B-LCP_PROVINCE
성      B-LCP_PROVINCE
창      B-LCP_CITY
##샤    B-LCP_CITY
(       B-LCP_CITY
長      B-LCP_CITY
[UNK]   B-LCP_CITY
)       B-LCP_CITY
시      B-LCP_CITY
우      B-LCP_CITY
##자    B-LCP_CITY
##링    B-LCP_CITY
(       B-LCP_CITY
五      B-LCP_CITY
家      B-LCP_CITY
[UNK]   B-LCP_CITY
)       B-LCP_CITY
가      B-LCP_CITY
한      O
시장    O
##에서  O
14      B-DT_DAY
##일    I-DT_DAY
```
