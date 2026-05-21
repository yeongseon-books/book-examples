# Harness Engineering 101 (2/10): Task Harness — 모호한 일을 실행 가능한 작업으로 바꾸기

Harness Engineering 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- 모호한 goal을 그대로 agent에게 주면 실행 단계에서 무엇이 깨질까요?
- Task Harness는 goal을 어떤 실행 단위와 완료 조건으로 번역해야 할까요?
- 좋은 task spec은 다음 agent 실행과 사람 리뷰에 어떤 증거를 남겨야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_example.py` | 예제 코드 |

## 실행 방법

```bash
cd harness-engineering-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-task-harness/step01_example.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/harness-engineering-101/ko/02-task-harness.md)
