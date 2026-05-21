# Azure Kubernetes Service 101 (3/7): 첫 클러스터 만들고 앱 배포하기 — Python/FastAPI

Azure Aks 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 실습용 AKS 클러스터를 만들 때 최소한 무엇을 결정해야 할까요?
- 기본 system pool 외에 user node pool을 왜 별도로 추가하는 편이 좋을까요?
- `az aks get-credentials` 이후 `kubectl`이 실제로 어떤 계층과 대화하게 될까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_first_cluster_commands.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-first-cluster-and-deploy/step01_first_cluster_commands.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-101/ko/03-first-cluster-and-deploy.md)
