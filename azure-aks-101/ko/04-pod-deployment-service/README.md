# Azure Kubernetes Service 101 (4/7): Pod·Deployment·Service — 워크로드를 표현하는 세 가지 방식

Azure Aks 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- Pod와 컨테이너는 왜 같은 말이 아니며, 왜 Kubernetes는 Pod를 스케줄링 단위로 볼까요?
- Deployment는 Pod를 직접 여러 개 만드는 것과 무엇이 다를까요?
- Service는 왜 Pod IP를 직접 쓰지 않게 만드는 걸까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_deployment_service_manifest.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-pod-deployment-service/step01_deployment_service_manifest.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-101/ko/04-pod-deployment-service.md)
