# AI Agent 101 (9/10): 운영

Ai Agent 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 운영 중 agent가 왜 그런 답을 냈는지 설명하려면 어떤 trace가 먼저 필요할까요?
- 비용과 latency는 어떤 단위로 측정해야 실제 병목이 보일까요?
- agent 배포와 rollback을 안전하게 만들려면 어떤 관측 지표가 gate가 되어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `snippet.py` | 예제 코드 |
| `snippet_04.py` | 예제 코드 |
| `snippet_05.py` | 예제 코드 |
| `step01_observability_cost.py` | 예제 코드 |
| `structured_logging.py` | 예제 코드 |
| `tracing.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-agent-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-production-operations/snippet.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-agent-101/ko/09-production-operations.md)
