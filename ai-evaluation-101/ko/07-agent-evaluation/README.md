# AI Evaluation 101 (7/10): 에이전트 평가하기 — 단일 응답이 아닌 trajectory

Ai Evaluation 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- agent 평가는 왜 단일 응답보다 trajectory를 함께 봐야 할까요?
- tool selection, step count, recovery metric은 각각 어떤 운영 리스크를 잡을까요?
- agent eval dashboard에는 어떤 step-level 신호가 반드시 들어가야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_agent_trajectory.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-agent-evaluation/step01_agent_trajectory.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-evaluation-101/ko/07-agent-evaluation.md)
