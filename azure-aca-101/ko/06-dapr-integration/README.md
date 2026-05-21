# Azure Container Apps 101 (6/7): Dapr 통합 — 사이드카로 얻는 것

Azure Aca 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- Dapr가 무엇이며, 그 사이드카는 ACA 안에서 정확히 어디에 붙을까요?
- App 수준 설정과 Environment 수준 component는 왜 분리해서 봐야 할까요?
- Service invocation, Pub/Sub, State store, Secret store 네 가지 핵심 구성요소는 각각 어떤 문제를 해결할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_dapr_sidecar.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-dapr-integration/step01_dapr_sidecar.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-101/ko/06-dapr-integration.md)
