# LLM API Production 101 (5/6): 재시도와 오류 처리 — 안정적인 API 호출 만들기

Llm Api Production 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 왜 모든 API 실패를 같은 재시도 정책으로 다루면 안 될까요?
- 어떤 오류는 재시도하고, 어떤 오류는 바로 실패로 분류해야 할까요?
- 최종 실패 뒤 사용자 메시지와 내부 로그는 어떻게 나눠야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_retry_backoff.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-api-production-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-retry-and-error-handling/step01_retry_backoff.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-api-production-101/ko/05-retry-and-error-handling.md)
