# Alembic 101 (3/10): 첫 revision: upgrade와 downgrade를 손으로 작성

Alembic 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- `alembic revision`이 만들어 주는 파일 구조는 어떻게 생겼을까요?
- `op.create_table`, `op.add_column`, `op.drop_column`, `op.execute`는 각각 언제 쓸까요?
- `upgrade()`와 `downgrade()`를 어떻게 대칭으로 유지할 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_upgrade_downgrade.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-first-revision-upgrade-downgrade/step01_upgrade_downgrade.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/03-first-revision-upgrade-downgrade.md)
