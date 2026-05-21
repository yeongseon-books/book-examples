# Alembic 101 (10/10): Production과 team workflow: PR, CI, 모니터링, 그리고 incident response

Alembic 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- one-revision-per-PR 원칙은 왜 중요할까요?
- Alembic-aware PR template과 CI checks는 어떻게 구성할까요?
- dev=SQLite, staging+prod=PostgreSQL 같은 multi-environment 전략은 어떻게 가져갈까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `3.py` | 예제 코드 |
| `health.py` | 예제 코드 |
| `migrate.yml` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `step01_team_workflow.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-production-and-team-workflow/3.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/10-production-and-team-workflow.md)
