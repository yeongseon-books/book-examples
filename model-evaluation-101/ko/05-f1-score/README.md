# Model Evaluation 101 (5/10): F1 점수

Model Evaluation 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- F1 점수를 운영 관점에서 볼 때 먼저 어떤 경계를 확인해야 할까요?
- F1 점수에서 예제나 다이어그램으로 검증해야 할 핵심 신호는 무엇일까요?
- F1 점수를 실제 시스템에 적용할 때 어떤 실패를 먼저 막아야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1.py` | 예제 코드 |
| `2_train_validation_test.py` | 예제 코드 |
| `confusion_matrix.py` | 예제 코드 |
| `confusion_matrix_09.py` | 예제 코드 |
| `pr.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_10.py` | 예제 코드 |
| `step01_fbeta_demo.py` | 예제 코드 |
| `threshold_roc.py` | 예제 코드 |

## 실행 방법

```bash
cd model-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-f1-score/1.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/model-evaluation-101/ko/05-f1-score.md)
