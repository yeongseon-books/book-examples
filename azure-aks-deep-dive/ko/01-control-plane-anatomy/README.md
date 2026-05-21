# Azure Kubernetes Service Deep Dive (1/6): Control Plane 해부 — AKS가 사용자에게서 가린 것

Azure Aks Deep Dive 시리즈 1편 예제 코드입니다.

## 학습 목표

- AKS control plane은 정확히 어떤 컴포넌트로 이루어져 있고, 사용자는 그중 무엇을 직접 볼 수 있을까요?
- 관리형 control plane이라는 약속은 어디까지를 의미하고, 어디부터는 여전히 사용자의 운영 책임일까요?
- API server SLA를 읽을 때 왜 `etcd`, scheduler, controller-manager의 내부 구현보다 API 표면을 먼저 봐야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_control_plane_boundary.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-control-plane-anatomy/step01_control_plane_boundary.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-deep-dive/ko/01-control-plane-anatomy.md)
