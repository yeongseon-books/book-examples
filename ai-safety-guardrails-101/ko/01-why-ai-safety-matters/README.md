# AI Safety & Guardrails 101 (1/10): AI Safety가 왜 중요한가

Ai Safety Guardrails 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- LLM 호출을 신뢰 경계 안쪽으로 두면 어떤 위험을 놓치게 될까요?
- Guardrail은 prompt 규칙과 무엇이 달라야 실제 안전장치가 될까요?
- 처음 운영에 넣을 최소 guardrail은 어디에 두어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_guardrail_baseline.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-why-ai-safety-matters/step01_guardrail_baseline.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/01-why-ai-safety-matters.md)
