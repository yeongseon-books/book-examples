# GitHub Actions 101 (7/10): Docker 빌드

Github Actions 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- Buildx는 왜 일반 빌더보다 더 자주 쓰일까요?
- GitHub Actions 캐시는 Docker 레이어 시간에 어떤 영향을 줄까요?
- GHCR에 푸시할 때 어떤 권한이 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_demo.py` | 예제 코드 |

## 실행 방법

```bash
cd github-actions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-docker-build/step01_demo.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/ko/07-docker-build.md)
