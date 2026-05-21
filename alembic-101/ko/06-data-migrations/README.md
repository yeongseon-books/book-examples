# Alembic 101 (6/10): 데이터 마이그레이션: schema 변경과 데이터 변경을 분리하기

Alembic 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- data migration은 schema migration과 무엇이 다를까요?
- `op.execute`는 raw SQL과 SQLAlchemy Core 중 어떤 스타일로 쓸 수 있을까요?
- 큰 데이터셋은 어떤 batch 패턴으로 나누어 처리해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1_schema_revision.py` | 예제 코드 |
| `2_data_backfill_revision.py` | 예제 코드 |
| `3_schema_tighten_revision.py` | 예제 코드 |
| `5.py` | 예제 코드 |
| `batch.py` | 예제 코드 |
| `op_execute.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_05.py` | 예제 코드 |
| `step01_data_backfill.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-data-migrations/1_schema_revision.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/06-data-migrations.md)
