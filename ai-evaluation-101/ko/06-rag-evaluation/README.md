# AI Evaluation 101 (6/10): RAG 시스템 평가하기

Ai Evaluation 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- RAG 평가는 왜 답변 하나가 아니라 retrieval과 generation을 나눠 봐야 할까요?
- context precision, context recall, faithfulness, answer relevance는 각각 무엇을 진단할까요?
- 검색과 생성 중 어디가 망가졌는지 어떻게 좁혀야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_rag_metrics.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-rag-evaluation/step01_rag_metrics.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-evaluation-101/ko/06-rag-evaluation.md)
