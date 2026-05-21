# Kubernetes 101 (2/10): Pod

Kubernetes 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- Pod와 컨테이너는 정확히 어떻게 다를까요?
- 왜 Kubernetes는 컨테이너가 아니라 Pod를 기본 단위로 삼을까요?
- 사이드카 패턴은 어떤 상황에서 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1_pod.py` | 예제 코드 |
| `2.py` | 예제 코드 |
| `3.py` | 예제 코드 |
| `4.py` | 예제 코드 |
| `pod.yaml` | 예제 코드 |
| `snippet.yaml` | 예제 코드 |
| `step01.py` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-pod/1_pod.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/02-pod.md)
