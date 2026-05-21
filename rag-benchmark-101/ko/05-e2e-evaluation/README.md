# RAG Evaluation and Benchmarking 101 (5/6): 종단 간 RAG 파이프라인 평가

Rag Benchmark 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 검색 지표가 좋아도 최종 답변이 나쁘면 어느 단계를 다시 봐야 할까요?
- 검색, 생성, 근거성 평가를 한 리포트에 묶으면 어떤 디버깅이 쉬워질까요?
- LLM-as-judge나 RAGAS 점수는 어떤 기준선 없이 쓰면 위험할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step1_pipeline.py` | 예제 코드 |
| `step2_evaluate_pipeline.py` | 예제 코드 |

## 실행 방법

```bash
cd rag-benchmark-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-e2e-evaluation/step1_pipeline.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/rag-benchmark-101/ko/05-e2e-evaluation.md)
