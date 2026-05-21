# Azure App Service Deep Dive (5/6): 스케일링 내부 동작 — Scale Out 결정과 워커 추가 경로

Azure App Service Deep Dive 시리즈 5편 예제 코드입니다.

## 학습 목표

- scale-up과 scale-out은 App Service에서 실제로 무엇을 바꿀까요?
- autoscale rule은 앱이 아니라 왜 App Service Plan에 붙는다고 봐야 할까요?
- Azure Monitor autoscale은 어떤 cadence와 observation window로 규칙을 평가할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_autoscale_loop.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-app-service-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-scaling-internals/step01_autoscale_loop.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-app-service-deep-dive/ko/05-scaling-internals.md)
