# Azure Container Apps Deep Dive (6/6): Envoy Ingress 경로 — 첫 요청이 사용자 컨테이너에 닿기까지

Azure Aca Deep Dive 시리즈 6편 예제 코드입니다.

## 학습 목표

- ACA의 public ingress 표면과 숨은 라우팅 계층은 어떻게 구분해 이해해야 할까요?
- TLS는 어디서 종료되고, 앱은 원래 요청 정보를 어떤 header로 복구할까요?
- Revision traffic split은 요청 경로의 어느 지점에서 실제가 될까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_ingress_path.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-envoy-ingress-path/step01_ingress_path.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-deep-dive/ko/06-envoy-ingress-path.md)
