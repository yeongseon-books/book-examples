# Kubernetes 101 (3/10): Deployment

Kubernetes 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- Deployment와 ReplicaSet은 어떤 관계일까요?
- `replicas`는 단순 숫자 이상의 어떤 의미를 가질까요?
- 이미지 변경이 왜 무중단 배포 흐름으로 이어질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `deployment.yaml` | 예제 코드 |
| `step01.py` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-deployment/deployment.yaml
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/03-deployment.md)
