# Alembic 101 (2/10): env.py와 target_metadata: 모델과 마이그레이션 연결

Alembic 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- `env.py`는 정확히 무엇이고 언제 실행될까요?
- 왜 `target_metadata`는 선택 사항이 아니라 필수일까요?
- DB URL을 환경 변수에서 안전하게 읽는 패턴은 어떻게 만들까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_env_target_metadata.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-env-py-and-target-metadata/step01_env_target_metadata.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/02-env-py-and-target-metadata.md)
