# Azure Kubernetes Service 101 (5/7): 네트워킹과 Ingress — 클러스터 안과 밖을 잇는 길

Azure Aks 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- Pod IP 할당 방식과 외부 HTTP 라우팅을 왜 별개의 문제로 봐야 할까요?
- kubenet, Azure CNI, Azure CNI Overlay는 각각 어떤 운영 trade-off를 가질까요?
- 새 AKS 클러스터에서 Azure CNI Overlay를 먼저 검토하는 이유는 무엇일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_ingress_manifest.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-networking-and-ingress/step01_ingress_manifest.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-101/ko/05-networking-and-ingress.md)
