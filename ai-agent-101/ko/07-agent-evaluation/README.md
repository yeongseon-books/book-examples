# AI Agent 101 (7/10): Agent 평가

Ai Agent 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- agent 평가는 왜 최종 답변 채점만으로 부족할까요?
- trajectory, tool-call accuracy, end-to-end success는 각각 어떤 실패를 잡아낼까요?
- 운영 전 eval set에는 어떤 실제 요청과 실패 사례를 넣어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `end_to_end.py` | 예제 코드 |
| `latency.py` | 예제 코드 |
| `latency_03.py` | 예제 코드 |
| `step01_eval_metrics.py` | 예제 코드 |
| `trajectory.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-agent-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-agent-evaluation/end_to_end.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-agent-101/ko/07-agent-evaluation.md)
