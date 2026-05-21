# Azure App Service Deep Dive (3/6): Worker 인스턴스와 샌드박스 — 사용자 코드를 어디에 가두는가

Azure App Service Deep Dive 시리즈 3편 예제 코드입니다.

## 학습 목표

- App Service의 worker는 실제로 어떤 실행 경계를 의미할까요?
- Windows code app에서 App Service sandbox는 무엇을 허용하고 무엇을 제한할까요?
- 왜 registry write와 GDI/User32 계열 제약이 Windows App Service에서 자주 문제를 만들까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_sandbox_profile.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-app-service-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-worker-and-sandbox/step01_sandbox_profile.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-app-service-deep-dive/ko/03-worker-and-sandbox.md)
