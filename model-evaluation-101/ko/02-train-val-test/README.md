# Model Evaluation 101 (2/10): 훈련·검증·테스트 데이터 나누기

Model Evaluation 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- train, validation, test는 각각 무엇을 맡아야 할까요?
- 왜 validation과 test를 같은 용도로 쓰면 안 될까요?
- 데이터 누수는 어떤 경로로 가장 자주 들어올까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_split_demo.py` | 예제 코드 |

## 실행 방법

```bash
cd model-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-train-val-test/step01_split_demo.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/model-evaluation-101/ko/02-train-val-test.md)
