# Docker 101 (2/10): Image와 Container

Docker 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- image와 container는 정확히 무엇이 다를까요?
- layer와 copy-on-write는 왜 중요한 개념일까요?
- 컨테이너의 수명 주기는 어떤 흐름으로 흘러갈까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_image_container_lifecycle.py` | 예제 코드 |

## 실행 방법

```bash
cd docker-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-image-and-container/step01_image_container_lifecycle.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/docker-101/ko/02-image-and-container.md)
