# Harness Engineering 101 (5/10): Tool Harness — Agent가 사용할 도구를 안전하게 설계하기

Harness Engineering 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- Tool Harness는 agent가 도구를 올바르게 쓰기 쉽도록 어떤 표면을 만들어야 할까요?
- schema, idempotency, actionable error는 각각 어떤 운영 문제를 줄일까요?
- 위험한 tool을 sandbox 안에 넣으려면 어떤 경계가 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_example.py` | 예제 코드 |

## 실행 방법

```bash
cd harness-engineering-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-tool-harness/step01_example.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/harness-engineering-101/ko/05-tool-harness.md)
