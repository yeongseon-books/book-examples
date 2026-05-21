# Azure Kubernetes Service 101 (6/7): 스케일링 — HPA, Cluster Autoscaler, KEDA

Azure Aks 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- HPA, Cluster Autoscaler, KEDA는 각각 어떤 신호를 보고 무엇을 바꿀까요?
- CPU나 메모리 기반 HPA만으로 부족한 상황은 언제일까요?
- Pod는 늘어났는데 응답이 바로 좋아지지 않는 이유는 어디에 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_scaling_manifests.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-scaling-hpa-ca-keda/step01_scaling_manifests.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-101/ko/06-scaling-hpa-ca-keda.md)
