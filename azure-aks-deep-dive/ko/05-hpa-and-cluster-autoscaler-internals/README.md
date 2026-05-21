# Azure Kubernetes Service Deep Dive (5/6): HPA와 Cluster Autoscaler 내부 — 두 컨트롤 루프

Azure Aks Deep Dive 시리즈 5편 예제 코드입니다.

## 학습 목표

- HPA는 어떤 메트릭을 어떤 주기로 읽고 desired replica를 계산할까요?
- Cluster Autoscaler는 어떤 신호를 보고 “새 노드가 필요하다”고 판단할까요?
- HPA와 Cluster Autoscaler가 동시에 움직일 때 race window는 왜 생길까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_hpa_ca_loops.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-hpa-and-cluster-autoscaler-internals/step01_hpa_ca_loops.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-deep-dive/ko/05-hpa-and-cluster-autoscaler-internals.md)
