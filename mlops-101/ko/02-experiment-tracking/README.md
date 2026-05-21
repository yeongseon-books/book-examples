# MLOps 101 (2/10): 실험 관리

Mlops 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- 실험 관리가 없으면 왜 같은 모델도 다시 만들기 어려울까요?
- 파라미터, 메트릭, 아티팩트, 환경 중 무엇을 반드시 남겨야 할까요?
- MLflow에서 experiment와 run은 어떤 관계로 이해하면 좋을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_experiment_tracking.py` | 예제 코드 |

## 실행 방법

```bash
cd mlops-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-experiment-tracking/step01_experiment_tracking.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/mlops-101/ko/02-experiment-tracking.md)
