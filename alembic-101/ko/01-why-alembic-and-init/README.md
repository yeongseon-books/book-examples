# Alembic 101 (1/10): 왜 Alembic인가, 그리고 init까지

Alembic 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- 마이그레이션 도구가 실제로 해결하는 문제는 무엇일까요?
- 왜 `Base.metadata.create_all`만으로는 운영 환경을 버틸 수 없을까요?
- revision, head, `alembic_version` 테이블은 각각 어떤 역할을 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `models.py` | 예제 코드 |
| `step01_why_init.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-why-alembic-and-init/models.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/01-why-alembic-and-init.md)
