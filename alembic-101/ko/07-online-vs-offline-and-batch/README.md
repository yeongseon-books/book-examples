# Alembic 101 (7/10): online과 offline 모드: --sql로 DDL을 미리 보고 SQLite batch 다루기

Alembic 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- Alembic이 제공하는 두 실행 모드, online과 offline은 어떻게 다를까요?
- `--sql`로 실제 SQL을 어떻게 미리 볼 수 있을까요?
- DBA 리뷰용 SQL 스크립트는 어떤 흐름으로 만들까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_online_offline_batch.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-online-vs-offline-and-batch/step01_online_offline_batch.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/07-online-vs-offline-and-batch.md)
