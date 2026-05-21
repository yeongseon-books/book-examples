# Model Evaluation 101 (6/10): ROC와 AUC 이해하기

Model Evaluation 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- ROC와 AUC 이해하기를 운영 관점에서 볼 때 먼저 어떤 경계를 확인해야 할까요?
- ROC와 AUC 이해하기에서 예제나 다이어그램으로 검증해야 할 핵심 신호는 무엇일까요?
- ROC와 AUC 이해하기를 실제 시스템에 적용할 때 어떤 실패를 먼저 막아야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `confusion_matrix.py` | 예제 코드 |
| `confusion_matrix_07.py` | 예제 코드 |
| `pr.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_05.py` | 예제 코드 |
| `snippet_08.py` | 예제 코드 |
| `step01_roc_pr_auc.py` | 예제 코드 |
| `threshold_roc.py` | 예제 코드 |

## 실행 방법

```bash
cd model-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-roc-and-auc/confusion_matrix.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/model-evaluation-101/ko/06-roc-and-auc.md)
