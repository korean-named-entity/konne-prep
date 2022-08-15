# konne-prep
한국어 중첩 개체명 말뭉치 준비 작업


- [klue-ner](klue-ner): klue-ner-v1.1의 오류를 수정한 말뭉치.
- [raw-sent](raw-sent): klue-ner의 원시 문장. klue-ner 수정에 따라 함께 갱신함.
- [ne-150-char-bio](ne-150-char-bio): klue-ner의 문장에 150개 부류 개체명을 자동 태깅한 결과.
- [konec](konec): ne-150-char-bio 결과를 수정하여 150부류 한국어 개체명 말뭉치 구축.     
- [konne-doccano](konne-doccano): konec을 doccano에서 작업할 수 있는 형식으로 변환하고 중첩 태깅.

원천 데이터인 KLUE-NER [klue-benchmark](https://klue-benchmark.com/tasks/69/overview/description)에서 데이터를 삭제하거나 추가하지 않고 주석 오류 수정, 150개의 부류로 확장 등의 추가 주석 작업을 통해 구축된 말뭉치


# [개체명 태그 세트 비교표](https://docs.google.com/spreadsheets/d/1k6eFkYMQl9UAhf5xT31-_BNQ5kMVZJZwMVhS6yAxRzk/edit?usp=sharing)       


150개 부류의 태그 세트의 명칭 등은 국립국어원  개체명  분석  말뭉치  개체  연결  버전  (2022).  2021( 1.0). 에 따라 주석하였음    
URL: https://corpus.korean.go.kr         


# Reference
If you find this dataset useful, please cite the following:

 {국문) 정유남, 송영숙, 유현조(2022), 2022년 세계 한국어 한마당 학술대회 발표자료집, 국어학회(발표 예정)                   
 (영문)  Yunam Cheong, Yongsook Song, Hyun-Jo You(2022), konne: A Korean Nested Named Entity Corpus, World convention of the Korean language, The Society of Korean Linguistics     

# V1의 최종은 다음 링크에 있는 데이터를 사용할 것을 추천드립니다.
https://github.com/korean-named-entity/konec 
               
