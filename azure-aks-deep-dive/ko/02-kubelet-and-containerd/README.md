# Azure Kubernetes Service Deep Dive (2/6): kubelet과 containerd — 노드 위에서 컨테이너가 뜨기까지

Azure Aks Deep Dive 시리즈 2편 예제 코드입니다.

## 학습 목표

- kubelet은 정확히 무엇을 감시하고 어떤 시점에 CRI를 호출할까요?
- dockershim이 사라진 뒤 AKS 노드 디버깅 방식은 왜 달라졌을까요?
- `RunPodSandbox`, `PullImage`, `CreateContainer`, `StartContainer`는 왜 이 순서로 호출될까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_kubelet_cri_path.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-kubelet-and-containerd/step01_kubelet_cri_path.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-deep-dive/ko/02-kubelet-and-containerd.md)
