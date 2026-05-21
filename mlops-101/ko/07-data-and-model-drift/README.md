# MLOps 101 (7/10): 데이터 드리프트와 모델 드리프트

Mlops 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- 데이터 드리프트와 모델 드리프트는 무엇이 다를까요?
- 왜 기준 분포를 잘못 잡으면 드리프트가 안 보이게 될까요?
- PSI와 KS 검정은 어떤 상황에서 유용할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_drift_detection.py` | 예제 코드 |

## 실행 방법

```bash
cd mlops-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-data-and-model-drift/step01_drift_detection.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/mlops-101/ko/07-data-and-model-drift.md)
