# Azure Container Apps Deep Dive (1/6): ACA 아키텍처 — 사용자에게 보이지 않는 Kubernetes 위에 얹은 것

Azure Aca Deep Dive 시리즈 1편 예제 코드입니다.

## 학습 목표

- ACA는 정확히 어떤 추상화 위에 어떤 추상화를 올린 서비스일까요?
- AKS와 비교할 때 Microsoft가 대신 떠안는 운영 책임과 사용자가 여전히 이해해야 할 책임은 무엇일까요?
- Environment는 단순한 상위 리소스가 아니라 왜 실제 격리 경계라고 봐야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_architecture_map.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-aca-architecture/step01_architecture_map.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-deep-dive/ko/01-aca-architecture.md)
