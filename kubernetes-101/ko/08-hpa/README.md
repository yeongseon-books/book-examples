# Kubernetes 101 (8/10): HPA

Kubernetes 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- 트래픽이 바뀔 때마다 사람이 직접 파드 수를 조절하면 왜 느리고 비싸질까요?
- HPA는 어떤 지표를 보고 스케일 아웃과 스케일 인을 결정할까요?
- resource requests가 없으면 왜 제대로 동작하지 않을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `hpa.yaml` | 예제 코드 |
| `step01.py` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-hpa/hpa.yaml
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/08-hpa.md)
