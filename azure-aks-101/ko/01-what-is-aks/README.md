# Azure Kubernetes Service 101 (1/7): Azure Kubernetes Service란? — 직접 운영하지 않아도 되는 Kubernetes

Azure Aks 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- AKS는 self-managed Kubernetes와 비교할 때 정확히 무엇을 대신 운영해 줄까요?
- 관리형 Kubernetes라고 해도 왜 여전히 `kubectl`, YAML, Service, Ingress를 이해해야 할까요?
- AKS 비용은 어디에서 발생하고, 왜 “클러스터 요금”보다 노드와 주변 리소스가 더 중요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_aks_summary.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-what-is-aks/step01_aks_summary.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-101/ko/01-what-is-aks.md)
