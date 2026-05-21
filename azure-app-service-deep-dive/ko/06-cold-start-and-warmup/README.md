# Azure App Service Deep Dive (6/6): 콜드 스타트와 Warmup — 첫 요청이 비싼 이유

Azure App Service Deep Dive 시리즈 6편 예제 코드입니다.

## 학습 목표

- App Service에서 cold start 비용은 실제로 어떤 준비 단계들의 합일까요?
- Always On은 어떤 종류의 coldness를 줄이고, 어떤 종류의 startup cost에는 거의 도움을 주지 못할까요?
- Windows와 Linux는 warm-up readiness를 어떤 다른 도구와 설정으로 표현할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_warmup_contract.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-app-service-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-cold-start-and-warmup/step01_warmup_contract.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-app-service-deep-dive/ko/06-cold-start-and-warmup.md)
