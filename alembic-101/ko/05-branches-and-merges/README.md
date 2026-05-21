# Alembic 101 (5/10): branch와 merge: 동시에 만든 revision을 합치는 법

Alembic 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 언제 Alembic revision graph가 branch로 갈라질까요?
- `branch_labels`와 `depends_on`은 각각 정확히 무슨 역할일까요?
- 두 개의 head를 `alembic merge`로 어떻게 합칠까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `4_cross_branch_dependency.py` | 예제 코드 |
| `5_branch.py` | 예제 코드 |
| `alembic_merge.py` | 예제 코드 |
| `branch_labels_depends_on.py` | 예제 코드 |
| `step01_branch_merge.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-branches-and-merges/4_cross_branch_dependency.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/05-branches-and-merges.md)
