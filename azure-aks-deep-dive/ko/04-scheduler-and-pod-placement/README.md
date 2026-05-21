# Azure Kubernetes Service Deep Dive (4/6): Scheduler와 Pod 배치 — 어느 노드로 갈지 누가 정하는가

Azure Aks Deep Dive 시리즈 4편 예제 코드입니다.

## 학습 목표

- kube-scheduler는 하나의 Pod에 대해 어떤 단계로 노드 후보를 좁혀 갈까요?
- `nodeSelector`, affinity, taint/toleration, topology spread는 서로 어떤 다른 의도를 표현할까요?
- Filter에서 모두 탈락한 경우와 feasible node는 있었지만 Binding이 실패한 경우는 어떻게 구분할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_scheduler_decision.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-scheduler-and-pod-placement/step01_scheduler_decision.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-deep-dive/ko/04-scheduler-and-pod-placement.md)
