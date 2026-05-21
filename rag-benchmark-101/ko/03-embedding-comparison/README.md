# RAG Evaluation and Benchmarking 101 (3/6): 임베딩 모델 비교

Rag Benchmark 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 임베딩 모델을 리더보드 점수만 보고 고르면 왜 위험할까요?
- 같은 corpus와 query에서 모델만 바꾸려면 어떤 조건을 고정해야 할까요?
- 품질이 좋아져도 latency나 비용이 커지면 어떻게 판단해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `compare_embeddings.py` | 예제 코드 |

## 실행 방법

```bash
cd rag-benchmark-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-embedding-comparison/compare_embeddings.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/rag-benchmark-101/ko/03-embedding-comparison.md)
