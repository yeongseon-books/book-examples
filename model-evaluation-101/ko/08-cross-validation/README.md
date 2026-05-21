# Model Evaluation 101 (8/10): 교차 검증 이해하기

Model Evaluation 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- 테스트 세트 점수 하나만으로 모델을 고르면 왜 불안정할까요?
- K-Fold는 어떤 아이디어 위에서 동작할까요?
- 왜 분류 문제에서는 stratified가 기본 선택이 될까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1.py` | 예제 코드 |
| `2_stratified_k_fold.py` | 예제 코드 |
| `3_groupkfold.py` | 예제 코드 |
| `4_timeseriessplit.py` | 예제 코드 |
| `5.py` | 예제 코드 |
| `confusion_matrix.py` | 예제 코드 |
| `confusion_matrix_10.py` | 예제 코드 |
| `pr.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_11.py` | 예제 코드 |
| `step01_cross_validation_demo.py` | 예제 코드 |
| `threshold_roc.py` | 예제 코드 |

## 실행 방법

```bash
cd model-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-cross-validation/1.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/model-evaluation-101/ko/08-cross-validation.md)
