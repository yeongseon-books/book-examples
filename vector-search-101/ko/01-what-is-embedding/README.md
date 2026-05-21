# Vector Search 101 (1/6): 임베딩이란 무엇인가 — 텍스트를 벡터로 변환하기

Vector Search 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- 키워드가 같은데도 검색 결과가 빗나가거나, 표현만 달라서 결과를 놓칠 때 무엇이 부족한 걸까요?
- 임베딩 벡터의 “가깝다”는 말은 실제로 무엇을 비교한다는 뜻일까요?
- 첫 모델을 고를 때 차원 수, 언어, 토큰 한도 중 무엇을 먼저 확인해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_first_vector.py` | 예제 코드 |

## 실행 방법

```bash
cd vector-search-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-what-is-embedding/step01_first_vector.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/vector-search-101/ko/01-what-is-embedding.md)
