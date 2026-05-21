# Azure App Service Deep Dive (1/6): App Service 플랫폼 아키텍처 — Front-End·Worker·File Server

Azure App Service Deep Dive 시리즈 1편 예제 코드입니다.

## 학습 목표

- App Service의 "플랫폼"은 실제로 어떤 박스들로 나눠서 이해해야 할까요?
- App Service Plan은 단순한 과금 단위가 아니라 어떤 격리와 용량의 의미를 가질까요?
- Front-End, Worker, shared storage는 각자 어떤 책임을 맡고 어디서 서로 연결될까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_architecture_map.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-app-service-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-platform-architecture/step01_architecture_map.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-app-service-deep-dive/ko/01-platform-architecture.md)
