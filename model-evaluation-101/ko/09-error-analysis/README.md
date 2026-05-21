# Model Evaluation 101 (9/10): 오류 분석으로 약점 찾기

Model Evaluation 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 전체 점수가 비슷한 두 모델은 어디에서 다르게 실패할까요?
- 슬라이스 분석은 어떤 약점을 드러내 줄까요?
- false positive와 false negative를 왜 나눠 봐야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1.py` | 예제 코드 |
| `2.py` | 예제 코드 |
| `3.py` | 예제 코드 |
| `4.py` | 예제 코드 |
| `confusion_matrix.py` | 예제 코드 |
| `confusion_matrix_10.py` | 예제 코드 |
| `pr.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_11.py` | 예제 코드 |
| `step01_error_analysis.py` | 예제 코드 |
| `threshold_roc.py` | 예제 코드 |

## 실행 방법

```bash
cd model-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-error-analysis/1.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/model-evaluation-101/ko/09-error-analysis.md)
