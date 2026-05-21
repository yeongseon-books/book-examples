# Vector Search 101 (6/6): 벡터 검색 파이프라인 — 문서 수집부터 쿼리까지

Vector Search 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 벡터 검색 파이프라인은 임베딩 한 번이 아니라 어떤 단계들의 연결일까요?
- 하이브리드 검색은 언제 단순 벡터 검색보다 안전할까요?
- 문서가 바뀌었을 때 재인덱싱과 운영 로그는 무엇을 기준으로 움직여야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_pipeline.py` | 예제 코드 |

## 실행 방법

```bash
cd vector-search-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-vector-search-pipeline/step01_pipeline.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/vector-search-101/ko/06-vector-search-pipeline.md)
