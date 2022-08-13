konec

# 한국어 개체명 말뭉치 

KLUE-NER에서 시작하여 150개 개체명 부류 태그를 추가 주석한 한국어 개체명 말뭉치

- [ne-150-char-bio](../ne-150-char-bio)의 결과에서 시작
- [work01-checkbio](#work01-checkbio): BIO 태그 형식 오류 수정


작업

- BIO 태그 중 I-태그 형식 오류 수정
- BIO 태그 중 B-태그 연쇄 오류 수정
- klue의 PS 정보를 이용한 태그 추가
- klue의 PS외 정보를 이용한 태그 추가
- konec의 kwic 생성. klue의 태그 정보를 병기
- konec과 klue가 불일치하는 경우를 중심으로 검토
- konec에서 false positive tag 삭제
- label 오류 수정
- span 오류 수정

## 작업

<a name="work01-checkbio"></a>

### BIO 태그 중 I-태그 형식 오류 수정

- I 태그가 B 태그 없이 나타난 오류가 2097건 존재한다.
- 단순히 I 태그를 B 태그로 수정하는 것으로는 적절하지 않은 경우가 많다.

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
갓	I-CV_POLICY             <-- ERROR:?B-CV_POLICY
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

### BIO 태그 중 B-태그 연쇄 오류 수정

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

### klue의 PS 정보를 이용한 태그 추가

klue에서 PS로 태깅이 되어 있는데 konec에서는 태깅이 되어있지 않은 항목을
대상으로 검토하여 태그 추가하였다. PS의 경우에 konec에서 주석이 누락된 경우가 
빈번하게 눈에 뜨이었으며 klue의 PS 태그가 상당히 정확한 것으로 판단되어 
klue의 PS를 활용하기로 하였다.

예를 들어, 다음의 "장백지"의 경우에 klue에는 PS로 태깅되어 있지만 konec에는
태깅이 되어 있지 않았다. 다음은 klue를 참조하여 konec을 수정한 예이다.

```
## klue-ner-v1_dev_00102-nsmc   어린시절 눈물 펑펑 흘리며 봤던 영화.. <장백지:PS>에 빠지게 했.던 영화...
...
장      B-PS    장      B-PS_NAME
백      I-PS    백      I-PS_NAME
지      I-PS    지      I-PS_NAME
..
```

- 컬럼1: klue token form
- 컬럼2: klue token bio
- 컬럼3: konec token form
- 컬럼4: konec token bio

### klue의 PS외 정보를 이용한 태그 추가

PS 외에도 klue에서 OG, LC, QT, DT, TI로 태깅이 되어있는데 konec에서는 아무런
태깅도 되지 않은 경우 klue의 정보를 활용하여 태그를 추가하기로 하였다.




## 메모

klue-konec 비교


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
