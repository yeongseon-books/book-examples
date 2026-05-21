# Docker 101 (3/10): Dockerfile 작성하기

Docker 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- `FROM`, `RUN`, `COPY`, `CMD`는 각각 어떤 역할을 할까요?
- Dockerfile 명령 순서는 왜 빌드 속도에 큰 영향을 줄까요?
- `.dockerignore`는 성능뿐 아니라 보안에도 왜 중요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_dockerfile_lint.py` | 예제 코드 |

## 실행 방법

```bash
cd docker-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-dockerfile/step01_dockerfile_lint.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/docker-101/ko/03-dockerfile.md)
