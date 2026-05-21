# AI Safety & Guardrails 101 (6/10): 독성과 편향 탐지

Ai Safety Guardrails 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 독성 차단과 편향 측정은 왜 같은 문제로 묶으면 안 될까요?
- 실시간 moderation과 offline audit은 각각 어떤 신호를 담당해야 할까요?
- false positive를 줄이면서 보호 기준을 유지하려면 무엇을 모니터링해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_toxicity_bias_scorer.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-toxicity-bias-detection/step01_toxicity_bias_scorer.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/06-toxicity-bias-detection.md)
