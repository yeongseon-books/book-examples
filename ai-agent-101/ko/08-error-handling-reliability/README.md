# AI Agent 101 (8/10): 에러 처리와 안정성

Ai Agent 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- agent 신뢰성을 볼 때 실패를 없애는 대신 무엇을 제어해야 할까요?
- Retry, fallback, circuit breaker는 각각 어떤 종류의 실패에 맞을까요?
- tool 실행을 안전하게 만들려면 실패 전후에 어떤 guard가 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `circuit_breaker.py` | 예제 코드 |
| `fallback_graceful_degradation.py` | 예제 코드 |
| `llm.py` | 예제 코드 |
| `retry.py` | 예제 코드 |
| `step01_retry_fallback.py` | 예제 코드 |
| `tool_recoverable.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-agent-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-error-handling-reliability/circuit_breaker.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-agent-101/ko/08-error-handling-reliability.md)
