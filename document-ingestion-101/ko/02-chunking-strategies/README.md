# Document Ingestion 101 (2/6): 청킹 전략 — 문서 유형별 최적화

Document Ingestion 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- 모든 문서에 같은 chunk_size를 쓰면 왜 검색 품질이 흔들릴까요?
- Recursive splitter는 어떤 순서로 경계를 포기하며 텍스트를 나눌까요?
- 임베딩 전에 청크 품질을 빠르게 검토하려면 무엇을 봐야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_fixed_vs_recursive.py` | 예제 코드 |
| `step02_heading_chunking.py` | 예제 코드 |

## 실행 방법

```bash
cd document-ingestion-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-chunking-strategies/step01_fixed_vs_recursive.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/document-ingestion-101/ko/02-chunking-strategies.md)
