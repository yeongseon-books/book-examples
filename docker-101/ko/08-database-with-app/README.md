# Docker 101 (8/10): 데이터베이스와 함께 실행하기

Docker 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- Compose로 PostgreSQL과 앱을 어떻게 함께 띄울까요?
- healthcheck와 시작 순서는 어떻게 연결해야 할까요?
- Alembic migration은 어떤 방식으로 자동화하는 편이 좋을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_db_compose_check.py` | 예제 코드 |

## 실행 방법

```bash
cd docker-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-database-with-app/step01_db_compose_check.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/docker-101/ko/08-database-with-app.md)
