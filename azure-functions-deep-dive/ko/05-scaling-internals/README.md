# Azure Functions Deep Dive (5/6): 스케일링 내부 동작 — Scale Controller, ScaleMonitor, 그리고 플랜별 차이

Azure Functions Deep Dive 시리즈 5편 예제 코드입니다.

## 학습 목표

- Consumption, Premium, Dedicated 플랜은 같은 스케일 의사결정 트리를 공유할까요?
- Scale Controller가 인스턴스를 더 늘리기로 결정하게 만드는 신호는 무엇일까요?
- burst 트래픽에서 scale-out 지연은 어디에 가장 많이 쌓일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_scaling.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-scaling-internals/step01_scaling.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-deep-dive/ko/05-scaling-internals.md)
