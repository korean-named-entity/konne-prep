# konne-prep
한국어 중첩 개체명 말뭉치 준비 작업

이 저장소는 한국어 중첩 개체명 말뭉치를 구축하는 준비 작업의 과정을 기록하고
중간 산출물들을 보존하기 위한 저장소입니다. 이 작업을 통해 구축된 결과물
데이터를 활용하고자 한다면 다음 저장소를 이용해 주십시오.

- [klue-v1-ner-fix](https://github.com/korean-named-entity/KLUE/tree/ner-fix): klue-ner-v1.1의 오류를 수정한 말뭉치
- [konec](https://github.com/korean-named-entity/konec ): klue-ner-v1의 원시 문장에 150개 세부류 개체명 주석을 부착한 말뭉치

준비 작업 과정의 기록:

- [klue-ner](klue-ner): klue-ner-v1.1의 오류를 수정한 말뭉치.
- [raw-sent](raw-sent): klue-ner의 원시 문장. klue-ner 수정에 따라 함께 갱신함.
- [ne-150-char-bio](ne-150-char-bio): klue-ner의 문장에 150개 부류 개체명을 자동 태깅한 결과.
- [konec](konec): ne-150-char-bio 결과를 수정하여 150부류 한국어 개체명 말뭉치 구축.     
- [konne-doccano](konne-doccano): konec을 doccano에서 작업할 수 있는 형식으로 변환하고 중첩 태깅.

## 태그셋

150개 부류의 태그 세트의 명칭 등은 국립국어원  개체명  분석  말뭉치  개체  연결  버전  (2022).  2021( 1.0). 에 따라 주석하였음    

- [개체명 태그 세트 비교표](https://docs.google.com/spreadsheets/d/1k6eFkYMQl9UAhf5xT31-_BNQ5kMVZJZwMVhS6yAxRzk/edit?usp=sharing)       
- [모두의 말뭉치](https://corpus.korean.go.kr)

## Reference

If you find this dataset useful, please cite the following:

- (국문) 정유남, 송영숙, 유현조(2022), 2022년 세계 한국어 한마당 학술대회 발표자료집, 국어학회(발표 예정)                   
- (영문)  Yunam Cheong, Yongsook Song, Hyun-Jo You(2022), konne: A Korean Nested Named Entity Corpus, World convention of the Korean language, The Society of Korean Linguistics     


               
