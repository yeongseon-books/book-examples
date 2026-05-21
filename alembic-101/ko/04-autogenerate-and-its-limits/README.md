# Alembic 101 (4/10): autogenerate: 잡는 것과 못 잡는 것의 경계

Alembic 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- `alembic revision --autogenerate`는 내부에서 무엇을 비교할까요?
- 어떤 변경은 잘 잡고, 어떤 변경은 놓치거나 옵션이 필요할까요?
- `compare_type`, `compare_server_default`, `include_object`, `include_name`은 언제 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `3.py` | 예제 코드 |
| `4_rename.py` | 예제 코드 |
| `compare_type_compare_server_default.py` | 예제 코드 |
| `include_object_include_name.py` | 예제 코드 |
| `models.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_04.py` | 예제 코드 |
| `step01_autogenerate_limits.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-autogenerate-and-its-limits/3.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/04-autogenerate-and-its-limits.md)
