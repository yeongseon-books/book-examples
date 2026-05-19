# backend-development-101

`backend-development-101` 시리즈의 예제 코드 저장소입니다. 각 에피소드 핵심 개념을 실행 가능한 최소 단위로 구성했으며, `ko/`와 `en/`은 동일 로직을 언어만 바꿔 미러링했습니다.

모든 예제는 offline mock-only 원칙을 따릅니다. 외부 API 호출, 실서비스 네트워크 연동, 클라우드 리소스 의존성 없이 로컬에서 재현 가능합니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python -m pytest tests/ -q
```

## 디렉터리 구조

- `common.py`: 공통 유틸리티(FastAPI 보조 함수, SQLite 모델, 인증 토큰, in-memory cache/queue)
- `ko/`: 한국어 에피소드별 예제(01~10)
- `en/`: 영어 에피소드별 예제(01~10, `ko/`와 동일 로직)
- `tests/`: 에피소드별 행동 테스트

## 에피소드 인덱스(원문)

1. [01-what-is-backend-development.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/01-what-is-backend-development.md)
2. [02-building-an-http-server.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/02-building-an-http-server.md)
3. [03-routing-and-controllers.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/03-routing-and-controllers.md)
4. [04-service-layer.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/04-service-layer.md)
5. [05-database-layer.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/05-database-layer.md)
6. [06-auth-and-authorization.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/06-auth-and-authorization.md)
7. [07-logging-and-error-handling.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/07-logging-and-error-handling.md)
8. [08-testing-the-backend.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/08-testing-the-backend.md)
9. [09-deploying-the-backend.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/09-deploying-the-backend.md)
10. [10-production-ready-backend.md](https://github.com/yeongseon-books/book-content/blob/master/content/backend-development-101/ko/10-production-ready-backend.md)

## 주의사항

- 이 저장소는 학습용 예제이며 offline mock-only입니다.
- DB는 in-memory SQLite만 사용합니다.
- 캐시와 큐는 외부 Redis/RabbitMQ 대신 in-memory 구현입니다.
