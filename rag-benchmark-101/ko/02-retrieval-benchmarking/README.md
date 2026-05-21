# RAG Evaluation and Benchmarking 101 (2/6): 검색 성능 측정

Rag Benchmark 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- 검색 성능을 감이 아니라 벤치마크 루프로 보려면 무엇을 고정해야 할까요?
- hit rate, MRR, latency는 검색기의 어떤 다른 측면을 측정할까요?
- 작은 gold set으로 시작해도 의미 있는 회귀 검사를 만들 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step1_corpus_queries.py` | 예제 코드 |
| `step2_run_benchmark.py` | 예제 코드 |

## 실행 방법

```bash
cd rag-benchmark-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-retrieval-benchmarking/step1_corpus_queries.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/rag-benchmark-101/ko/02-retrieval-benchmarking.md)
