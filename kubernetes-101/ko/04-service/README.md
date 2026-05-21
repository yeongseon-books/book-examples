# Kubernetes 101 (4/10): Service

Kubernetes 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- Service는 정확히 어떤 문제를 해결할까요?
- ClusterIP, NodePort, LoadBalancer는 언제 갈라질까요?
- selector와 labels는 왜 정확히 맞아야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1_service.py` | 예제 코드 |
| `2.py` | 예제 코드 |
| `3_dns.py` | 예제 코드 |
| `4_nodeport.py` | 예제 코드 |
| `service.yaml` | 예제 코드 |
| `snippet.yaml` | 예제 코드 |
| `step01.py` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-service/1_service.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/04-service.md)
