ne-150-char-bio

# 개체명 150 부류 자동 태깅 결과

- [ne-150-subword-bio](ne-150-subword-bio): klue-ner-v1.1에 150개 부류 개체명 자동 태깅한 결과. subword BIO 형식.
- subword BIO 형식을 char BIO 형식으로 변환 
- klue-ner-v1.1과 짝을 맞춤
 

## 변환

- [raw-sent](../raw-sent)의 원시 문장을 기준으로
- [ne-150-subword-bio](ne-150-subword-bio)의 태깅 결과를 정리하여
- 각 음절문자에 BIO 태그를 부착한다.

다음 명령으로 두 파일을 생성할 수 있다. 

```
$ make all
```

- [ne-dev-150-char-bio.tsv](ne-dev-150-char-bio.tsv)
- [ne-train-150-char-bio.tsv](ne-train-150-char-bio.tsv)


변환 결과를 예시하면 아래와 같다.

- 헤더 5행은 klue-ner-v1과 동일하게 유지하였다.
- `## klue-ner-v1_train_00000_wikitree`와 같이 문장 아이디는 klue-ner-v1과 동일하게 유지하였다.
- 문장번호와 함께 원시문장을 제시하였다. 인라인 태그 형식으로 제시된 klue-ner-v1과 다른 점이다.
- 음절문자와 BIO 태그를 탭으로 구분하여 나열하였다. klue-ner-v1과 동일하다. 

```
## 토큰, 레이블 구분자 : \t
## 토큰 구분자 : \n
## 문장 구분자 : \n\n
## 주석 : ##
## 컬럼명 : CHAR	NE_TAG
## klue-ner-v1_train_00000_wikitree	특히 영동고속도로 강릉 방향 문막휴게소에서 만종분기점까지 5km 구간에는 승용차 전용 임시 갓길차로제를 운영하기로 했다.
특	O
히	O
 	O
영	B-AF_ROAD
동	I-AF_ROAD
고	I-AF_ROAD
속	I-AF_ROAD
도	I-AF_ROAD
로	I-AF_ROAD
 	O
강	B-LCP_CITY
릉	I-LCP_CITY
 	O
방	O
향	O
 	O
문	B-LC_OTHERS
막	I-LC_OTHERS
휴	I-LC_OTHERS
게	I-LC_OTHERS
소	I-LC_OTHERS
```

## 변환 결과 검증

변환 과정에 문제가 없는지 검증하기 위하여 다음과 같이 검증용 파일을 생성할 수
있다.

```
$ make valid
```

원시문장 [raw-sent](../raw-sent)과 [ne-150-subword-bio](ne-150-subword-bio)의
문자 대 문자 대응 관계를 확인할 수 있다. 결과를 예시하면 아래와 같다.

- 컬럼 1: 
  - `=`는 일치를 의미한다.
  - `u`는 ne-150-subword 출력 결과가 `UNK`인 경우이다.
  - `s`는 원시문장에 공백문자가 있는 경우이다. ne-150-suword에는 공백문자가 없다.
  - `x`는 불일치를 의미한다.
- 컬럼 2: 원시문장의 음절문자
- 컬럼 3: ne-150-subword의 음절문자
- 컬럼 4: ne-150-subword의 BIO 태그

```
## klue-ner-v1_train_00094_wikitree	이번 쓰촨 대지진 역시 아침 8시 2분에 예고없이 일어났으며, 중국매체들은 지진 참사 상황에서 중국인들이 보여준 다양한 모습들을 소개했습니다.
=	이	이	O
=	번	번	O
us	 	UNK	O
u	쓰	UNK	B-EV_OTHERS
u	촨	UNK	I-EV_OTHERS
s	 	 	I-EV_OTHERS
=	대	대	I-EV_OTHERS
=	지	지	I-EV_OTHERS
=	진	진	I-EV_OTHERS
s	 	 	O
=	역	역	O
=	시	시	O
s	 	 	O
=	아	아	B-TI_OTHERS
=	침	침	I-TI_OTHERS
s	 	 	I-TI_OTHERS
=	8	8	I-TI_OTHERS
=	시	시	I-TI_OTHERS
s	 	 	I-TI_OTHERS
=	2	2	I-TI_OTHERS
=	분	분	I-TI_OTHERS
=	에	에	O
```




