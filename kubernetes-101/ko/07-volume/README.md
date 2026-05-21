# Kubernetes 101 (7/10): Volume

Kubernetes 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- 파드가 재시작되면 컨테이너 파일시스템은 왜 사라질까요?
- `emptyDir`와 PVC는 어떤 순간에 갈라질까요?
- StorageClass는 단순 옵션이 아니라 무엇을 결정할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01.py` | 예제 코드 |
| `volume.yaml` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-volume/step01.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/07-volume.md)
