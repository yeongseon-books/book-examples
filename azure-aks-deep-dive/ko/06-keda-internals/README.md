# Azure Kubernetes Service Deep Dive (6/6): KEDA 내부 — ScaledObject가 HPA를 만드는 방식

Azure Aks Deep Dive 시리즈 6편 예제 코드입니다.

## 학습 목표

- KEDA는 ScaledObject를 어떻게 generated HPA로 바꾸고, 그 과정에서 무엇을 보장할까요?
- metrics adapter는 external metrics 경로에서 어디까지를 책임질까요?
- scaler 인터페이스는 이벤트 소스에 어떤 질문을 던질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_keda_scaledobject_flow.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-keda-internals/step01_keda_scaledobject_flow.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-deep-dive/ko/06-keda-internals.md)
