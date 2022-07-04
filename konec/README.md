konec

# 한국어 개체명 말뭉치 

- [ne-150-char-bio](../ne-150-char-bio)의 결과에서 시작

계획


- konec 형식 오류 수정
- klue-ner과 일대일로 매핑
- span이 일치하면서 대부류 태그가 불일치하는 경우 확인
- span이 불일치하는 경우 확인

## konec 자체 오류 수정
### 형식 오류 수정

- I 태그가 B 태그 없이 나타난 오류가 상당수 존재한다.

```
## klue-ner-v1_train_00000_wikitree	특히 영동고속도로 강릉 방향 문막휴게소에서 만종분기점까지 5km 구간에는 승용차 전용 임시 갓길차로제를 운영하기로 했다.
...
승	B-AF_TRANSPORT
용	I-AF_TRANSPORT
차	I-AF_TRANSPORT
 	O
전	O
용	O
 	O
임	O
시	O
 	O
갓	I-CV_POLICY             <-- ERROR: B-CV_POLICY
길	I-CV_POLICY
차	I-CV_POLICY
로	I-CV_POLICY
제	I-CV_POLICY
를	O
 	O
운	O
영	O
하	O
기	O
로	O
```

### B 태그가 불필요하게 연달아 나타나는 오류

```
## klue-ner-v1_train_00010_wikitree	중국 후난(湖南)성 창샤(長沙)시 우자링(五家岭)가 한 시장에서 14일 오전 10시 15분께 칼부림 사건이 일어나 5명이 숨지고 1명이 부상했다고 중신넷이 14일 보도했다.
중	B-LCP_COUNTRY
국	I-LCP_COUNTRY
 	O
후	B-LCP_PROVINCE
난	B-LCP_PROVINCE     <- ERROR: I-LCP_PROVINCE
(	B-LCP_PROVINCE
湖	B-LCP_PROVINCE
南	B-LCP_PROVINCE
)	B-LCP_PROVINCE
성	B-LCP_PROVINCE
 	O
창	B-LCP_CITY
샤	B-LCP_CITY
(	B-LCP_CITY
長	B-LCP_CITY
沙	B-LCP_CITY
)	B-LCP_CITY
시	B-LCP_CITY
```

## klue-konec 비교 

### 누락

```
핸	O	핸	B-TMI_HW
드	O	드	I-TMI_HW
폰	O	폰	I-TMI_HW
 	O	 	O
배	O	배	O
경	O	경	O
 	O	 	O
화	O	화	O
면	O	면	O
이	O	이	O
 	O	 	O
미	B-PS	미	O
란	I-PS	란	O
다	I-PS	다	O
 	I-PS	 	O
커	I-PS	커	O
라	O	라	O
는	O	는	O
```


### klue-konec 정보 통합?

```
프	B-LC	프	B-CV_ART
랑	I-LC	랑	I-CV_ART
스	I-LC	스	I-CV_ART
영	O	영	I-CV_ART
화	O	화	I-CV_ART
는	O	는	O
```


### klue-konec span 불일치? (konec은 조사 경계를 잘 파악하지 못하는 경향이 보임)

```
2	B-QT	2	B-QT_LENGTH
1	I-QT	1	I-QT_LENGTH
8	I-QT	8	I-QT_LENGTH
야	I-QT	야	I-QT_LENGTH
드	I-QT	드	I-QT_LENGTH
로	O	로	I-QT_LENGTH
 	O	 	O
세	O	세	O
팅	O	팅	O
된	O	된	O
 	O	 	O
8	B-QT	8	B-QT_ORDER
번	I-QT	번	I-QT_ORDER
홀	O	홀	I-QT_ORDER
에	O	에	O
서	O	서	O
```

### klue-konec span 불일치? (konec은 조사 경계를 잘 파악하지 못하는 경향이 보임)

```
8	B-QT	8	B-QT_MAN_COUNT
만	I-QT	만	I-QT_MAN_COUNT
 	I-QT	 	I-QT_MAN_COUNT
명	I-QT	명	I-QT_MAN_COUNT
의	O	의	I-QT_MAN_COUNT
 	O	 	O
인	O	인	O
파	O	파	O
```

### konec 태그 오류 

```
걘	O	걘	B-AFA_VIDEO
적	O	적	I-AFA_VIDEO
으	O	으	I-AFA_VIDEO
로	O	로	I-AFA_VIDEO
 	O	 	O
```  

### konec 태그 범위와 분류 복합적 오류

```
톰	B-PS	톰	B-PS_NAME
아	O	아	I-PS_NAME
저	O	저	I-PS_NAME
씨	O	씨	O
```

월	B-OG	월	B-AFA_VIDEO
트	I-OG	트	I-AFA_VIDEO
디	I-OG	디	I-AFA_VIDEO
즈	I-OG	즈	I-AFA_VIDEO
니	I-OG	니	O
```
