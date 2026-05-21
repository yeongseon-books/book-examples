# Docker 101 (10/10): 배포용 Docker 구성

Docker 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- 프로덕션에서는 어떤 이미지 태그 정책을 가져가야 할까요?
- 레지스트리와 이미지 서명은 왜 공급망 신뢰의 일부일까요?
- read-only, capability 제한, non-root는 어떤 식으로 결합해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_production_policy_check.py` | 예제 코드 |

## 실행 방법

```bash
cd docker-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-production-docker/step01_production_policy_check.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/docker-101/ko/10-production-docker.md)
