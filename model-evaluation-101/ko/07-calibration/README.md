# Model Evaluation 101 (7/10): 확률 보정 이해하기

Model Evaluation 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- 모델이 예측한 확률을 왜 그대로 믿으면 안 될까요?
- 신뢰도 곡선은 무엇을 보여 줄까요?
- Brier 점수는 어떤 종류의 오류를 요약할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1.py` | 예제 코드 |
| `2.py` | 예제 코드 |
| `4_platt.py` | 예제 코드 |
| `confusion_matrix.py` | 예제 코드 |
| `confusion_matrix_10.py` | 예제 코드 |
| `pr.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_11.py` | 예제 코드 |
| `step01_calibration_demo.py` | 예제 코드 |
| `threshold_roc.py` | 예제 코드 |

## 실행 방법

```bash
cd model-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-calibration/1.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/model-evaluation-101/ko/07-calibration.md)
