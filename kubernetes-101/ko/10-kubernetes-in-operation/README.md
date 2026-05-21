# Kubernetes 101 (10/10): 운영 관점의 Kubernetes

Kubernetes 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- liveness, readiness, startup probe는 어떤 역할을 나눌까요?
- RBAC와 NetworkPolicy는 왜 운영의 기본 경계일까요?
- 메트릭, 로그, 트레이스는 왜 함께 봐야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1.py` | 예제 코드 |
| `2_rbac.py` | 예제 코드 |
| `3_networkpolicy.py` | 예제 코드 |
| `4.py` | 예제 코드 |
| `5.py` | 예제 코드 |
| `ops.yaml` | 예제 코드 |
| `snippet.yaml` | 예제 코드 |
| `step01.py` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-kubernetes-in-operation/1.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/10-kubernetes-in-operation.md)
