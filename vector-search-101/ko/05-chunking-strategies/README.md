# Vector Search 101 (5/6): 청크 전략 — 긴 문서를 어떻게 나눌 것인가

Vector Search 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 긴 문서를 그대로 임베딩하지 않고 왜 청크로 나눠야 할까요?
- chunk_size와 overlap은 검색 품질과 비용 사이에서 어떤 균형을 만들까요?
- 청크에 메타데이터를 붙이지 않으면 답변 경로에서 무엇이 막힐까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_chunking_and_search.py` | 예제 코드 |

## 실행 방법

```bash
cd vector-search-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-chunking-strategies/step01_chunking_and_search.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/vector-search-101/ko/05-chunking-strategies.md)
