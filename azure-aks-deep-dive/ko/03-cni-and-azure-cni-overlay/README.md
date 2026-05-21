# Azure Kubernetes Service Deep Dive (3/6): CNI와 Azure CNI Overlay — Pod IP가 어디서 오는가

Azure Aks Deep Dive 시리즈 3편 예제 코드입니다.

## 학습 목표

- kubenet, Azure CNI Pod Subnet, Azure CNI Node Subnet, Azure CNI Overlay는 IP 소비와 라우팅 면에서 무엇이 다를까요?
- Pod IP가 실제 VNet 공간을 직접 소비할 때 어떤 운영 한계가 가장 먼저 드러날까요?
- Overlay 모드에서는 Pod에서 외부로 나가는 트래픽이 어떤 SNAT 경로를 거칠까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_network_mode_model.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-cni-and-azure-cni-overlay/step01_network_mode_model.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-deep-dive/ko/03-cni-and-azure-cni-overlay.md)
