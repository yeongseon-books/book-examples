# RAG Evaluation and Benchmarking 101 (4/6): VectorDB 선택 기준

Rag Benchmark 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- VectorDB는 기능 목록이 아니라 어떤 운영 조건으로 비교해야 할까요?
- 같은 임베딩과 corpus에서 VectorDB만 바꿔 보려면 무엇을 고정해야 할까요?
- 정확도, latency, 필터링, 운영 복잡도가 충돌할 때 어떤 기준으로 선택해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `faiss_benchmark.py` | 예제 코드 |

## 실행 방법

```bash
cd rag-benchmark-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-vectordb-selection/faiss_benchmark.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/rag-benchmark-101/ko/04-vectordb-selection.md)
