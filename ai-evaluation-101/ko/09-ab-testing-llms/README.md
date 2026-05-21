# AI Evaluation 101 (9/10): LLM A/B 테스팅 — 어느 prompt가 더 나은가

Ai Evaluation 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- LLM A/B 테스트는 왜 “더 좋아 보인다”는 감상이 아니라 통계적 의사결정이어야 할까요?
- win rate, sample size, statistical significance는 각각 어떤 판단을 도와줄까요?
- 온라인 A/B에서 사용자 위험을 줄이려면 어떤 guardrail metric이 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `effect_size.py` | 예제 코드 |
| `online_analysis.py` | 예제 코드 |
| `online_router.py` | 예제 코드 |
| `pairwise_winrate.py` | 예제 코드 |
| `sample_size.py` | 예제 코드 |
| `significance.py` | 예제 코드 |
| `step01_ab_welch.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-ab-testing-llms/effect_size.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-evaluation-101/ko/09-ab-testing-llms.md)
