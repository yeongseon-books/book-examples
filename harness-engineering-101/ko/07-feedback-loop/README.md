# Harness Engineering 101 (7/10): Feedback Loop — 실패를 고치게 만드는 반복 구조

Harness Engineering 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- Feedback Loop는 실패를 종료 신호가 아니라 어떤 입력으로 바꿔야 할까요?
- 단순 retry와 reflect는 어디서 갈라지고, 언제 각각 써야 할까요?
- 무한 루프를 막으려면 반복 안에 어떤 제한과 기억을 남겨야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_example.py` | 예제 코드 |

## 실행 방법

```bash
cd harness-engineering-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-feedback-loop/step01_example.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/harness-engineering-101/ko/07-feedback-loop.md)
