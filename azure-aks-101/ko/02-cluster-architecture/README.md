# Azure Kubernetes Service 101 (2/7): 클러스터 아키텍처 — Control Plane과 Node Pool

Azure Aks 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- API server, scheduler, controller manager, etcd는 각각 어떤 일을 할까요?
- Node Pool은 단순한 VM 묶음 이상으로 왜 중요한 관리 단위일까요?
- system node pool과 user node pool을 분리해야 하는 실무적 이유는 무엇일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_node_pool_layout.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-cluster-architecture/step01_node_pool_layout.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-101/ko/02-cluster-architecture.md)
