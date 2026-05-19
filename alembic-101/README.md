# alembic-101

`alembic-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 실행 가능한 SQLite/in-memory 기반으로 구성되어 있으며, Alembic의 핵심 개념을 에피소드별로 작게 검증할 수 있게 설계했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-why-alembic-and-init/step01_why_init.py
python en/10-production-and-team-workflow/step01_team_workflow.py
python -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py` - SQLite in-memory 엔진, 임시 Alembic 환경, 버전 테이블 헬퍼
- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 행동 테스트

## 에피소드 인덱스 (원문 링크)

- [01 왜 Alembic인가, 그리고 init까지](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/01-why-alembic-and-init.md)
- [02 env.py와 target_metadata](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/02-env-py-and-target-metadata.md)
- [03 첫 revision: upgrade와 downgrade](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/03-first-revision-upgrade-downgrade.md)
- [04 autogenerate 한계](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/04-autogenerate-and-its-limits.md)
- [05 branch와 merge](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/05-branches-and-merges.md)
- [06 데이터 마이그레이션](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/06-data-migrations.md)
- [07 online/offline과 batch](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/07-online-vs-offline-and-batch.md)
- [08 downgrade 전략](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/08-downgrade-strategy.md)
- [09 배포 순서와 blue/green](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/09-deploy-ordering-and-blue-green.md)
- [10 production과 팀 워크플로우](https://github.com/yeongseon-books/book-content/blob/master/content/alembic-101/ko/10-production-and-team-workflow.md)

## 주의사항

- 이 저장소는 학습용 mock 예제입니다.
- 외부 DB(PostgreSQL 등)나 외부 API 의존성 없이 동작합니다.

## License

MIT
