# Vector Search 101 (3/6): 코사인 유사도와 벡터 검색 — 문장 간 거리 계산하기

Vector Search 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 벡터가 있으면 왜 바로 검색이 끝나는 게 아니라 거리 척도를 골라야 할까요?
- 코사인 유사도와 내적, L2 거리는 결과를 어떻게 다르게 만들까요?
- 정규화 여부가 검색 순위와 FAISS 인덱스 선택에 왜 영향을 줄까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_distance_metrics.py` | 예제 코드 |

## 실행 방법

```bash
cd vector-search-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-cosine-similarity/step01_distance_metrics.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/vector-search-101/ko/03-cosine-similarity.md)
