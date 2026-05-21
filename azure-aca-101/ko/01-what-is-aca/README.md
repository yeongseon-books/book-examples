# Azure Container Apps 101 (1/7): Azure Container Apps란? — Kubernetes 없이 컨테이너 운영하기

Azure Aca 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- Azure Container Apps(ACA)는 다른 Azure 컨테이너 서비스(App Service, AKS, Functions)와 무엇이 다를까요?
- ACA의 세 가지 핵심 구성 요소인 Environment, Container App, Revision은 각각 어떤 역할을 할까요?
- 어떤 워크로드는 ACA에 잘 맞고, 어떤 워크로드는 다른 서비스에 두는 편이 나을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_aca_positioning.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-what-is-aca/step01_aca_positioning.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-101/ko/01-what-is-aca.md)
