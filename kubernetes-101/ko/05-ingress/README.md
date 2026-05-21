# Kubernetes 101 (5/10): Ingress

Kubernetes 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- Ingress와 IngressController는 왜 따로 이해해야 할까요?
- 여러 서비스를 하나의 도메인 아래에서 어떻게 나눌 수 있을까요?
- `host`, `path`, `pathType`은 어떤 차이를 만들까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1_ingress.py` | 예제 코드 |
| `2.py` | 예제 코드 |
| `3_tls.py` | 예제 코드 |
| `4_tls.py` | 예제 코드 |
| `5.py` | 예제 코드 |
| `ingress.yaml` | 예제 코드 |
| `snippet.yaml` | 예제 코드 |
| `step01.py` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-ingress/1_ingress.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/05-ingress.md)
