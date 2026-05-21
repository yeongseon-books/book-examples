# RAG Evaluation and Benchmarking 101 (1/6): RAG 평가 지표 이해

Rag Benchmark 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- RAG 답변이 틀렸을 때 검색 문제와 생성 문제를 어떻게 분리할 수 있을까요?
- Precision@k, Recall@k, MRR는 같은 결과 목록에서 각각 어떤 실패를 보여 줄까요?
- 평균 점수만 보면 왜 질문별 실패 패턴을 놓칠 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step1_retrieval_metrics.py` | 예제 코드 |
| `step2_llm_judge.py` | 예제 코드 |

## 실행 방법

```bash
cd rag-benchmark-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-evaluation-metrics/step1_retrieval_metrics.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/rag-benchmark-101/ko/01-evaluation-metrics.md)
