# Docker 101 (7/10): Python 앱 컨테이너화

Docker 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- FastAPI와 uvicorn을 어떤 방식으로 컨테이너에 담아야 할까요?
- PID 1과 SIGTERM은 왜 컨테이너 운영에서 중요할까요?
- healthcheck는 어떻게 구성해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_python_container_check.py` | 예제 코드 |

## 실행 방법

```bash
cd docker-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-python-app-containerize/step01_python_container_check.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/docker-101/ko/07-python-app-containerize.md)
