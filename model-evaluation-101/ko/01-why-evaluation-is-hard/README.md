# Model Evaluation 101 (1/10): 모델 평가는 왜 어려운가?

Model Evaluation 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- 왜 정확도 하나만으로 모델을 판단하면 위험할까요?
- 데이터 분포와 베이스레이트는 평가를 어떻게 왜곡할까요?
- 임계값이 바뀌면 같은 모델의 점수는 왜 달라질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1.py` | 예제 코드 |
| `4.py` | 예제 코드 |
| `5.py` | 예제 코드 |
| `confusion_matrix.py` | 예제 코드 |
| `confusion_matrix_10.py` | 예제 코드 |
| `pr.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_11.py` | 예제 코드 |
| `step01_leakage_demo.py` | 예제 코드 |
| `threshold_roc.py` | 예제 코드 |

## 실행 방법

```bash
cd model-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-why-evaluation-is-hard/1.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/model-evaluation-101/ko/01-why-evaluation-is-hard.md)
