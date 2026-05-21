# Kubernetes 101 (1/10): Kubernetes란 무엇인가?

Kubernetes 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- 오케스트레이션이라는 말은 실제로 무엇을 대신해 줄까요?
- 컨트롤 플레인과 워커 노드는 어떤 식으로 역할을 나눌까요?
- 원하는 상태 모델이 왜 Kubernetes의 핵심 철학일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `pod.yaml` | 예제 코드 |
| `step01.py` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-what-is-kubernetes/pod.yaml
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/01-what-is-kubernetes.md)
