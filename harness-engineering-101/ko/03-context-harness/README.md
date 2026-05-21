# Harness Engineering 101 (3/10): Context Harness — Agent에게 줄 정보와 숨길 정보 설계하기

Harness Engineering 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- Context Harness는 왜 무한한 메모리가 아니라 제한된 예산 배분 문제일까요?
- agent에게 보여줄 정보와 숨길 정보는 어떤 기준으로 나눠야 할까요?
- retrieved context가 많아질수록 정밀도는 어떻게 지켜야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_example.py` | 예제 코드 |

## 실행 방법

```bash
cd harness-engineering-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-context-harness/step01_example.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/harness-engineering-101/ko/03-context-harness.md)
