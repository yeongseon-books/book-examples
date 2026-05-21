# AI Safety & Guardrails 101 (7/10): Hallucination Guardrail — Grounding 검증

Ai Safety Guardrails 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- Hallucination guardrail은 왜 답변 전체가 아니라 주장 단위로 봐야 할까요?
- claim extraction, entailment check, citation format은 각각 무엇을 검증할까요?
- 근거가 부족한 답변은 차단, 수정, 보류 중 어디로 보내야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_grounding_check.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-hallucination-guardrails/step01_grounding_check.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/07-hallucination-guardrails.md)
