# Alembic 101 (8/10): downgrade 전략: 언제 진심으로 작성하고 언제 막을 것인가

Alembic 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- production에서 downgrade는 언제 가능하고 언제 사실상 불가능할까요?
- 어떤 종류의 변경이 irreversible하며, 어떻게 다뤄야 할까요?
- expand-contract는 downgrade 가능성을 어떻게 회복시킬까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_downgrade_policy.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-downgrade-strategy/step01_downgrade_policy.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/08-downgrade-strategy.md)
