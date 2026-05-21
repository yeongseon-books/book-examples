# MLOps 101 (5/10): 모델 배포

Mlops 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 학습된 모델 파일을 어떻게 사용자 요청에 연결할 수 있을까요?
- 온라인 추론, 배치 추론, 스트리밍 추론은 어떤 차이로 이해하면 좋을까요?
- FastAPI와 Docker는 모델 배포에서 어떤 역할을 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_model_deployment.py` | 예제 코드 |

## 실행 방법

```bash
cd mlops-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-model-deployment/step01_model_deployment.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/mlops-101/ko/05-model-deployment.md)
