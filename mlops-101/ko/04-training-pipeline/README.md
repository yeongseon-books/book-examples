# MLOps 101 (4/10): 모델 학습 파이프라인

Mlops 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- 학습 스크립트 하나를 여러 단계 파이프라인으로 나누는 이유는 무엇일까요?
- DAG는 단순 실행 순서와 어떻게 다를까요?
- Airflow, Prefect, Kubeflow 같은 오케스트레이터는 어디에 들어갈까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_training_pipeline.py` | 예제 코드 |

## 실행 방법

```bash
cd mlops-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-training-pipeline/step01_training_pipeline.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/mlops-101/ko/04-training-pipeline.md)
