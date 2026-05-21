# Harness Engineering 101 (4/10): Constraint Harness — 규칙, 경계, 금지 행동 정의하기

Harness Engineering 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- Constraint Harness는 prompt 규칙과 무엇이 달라야 실제로 agent 행동을 제한할까요?
- capability, resource, behavior, scope 제약은 각각 어떤 위험을 막을까요?
- 제약이 실행 계약이 되려면 코드와 로그에 무엇이 남아야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `4.py` | 예제 코드 |
| `behavioral_constraints.py` | 예제 코드 |
| `capability_constraints.py` | 예제 코드 |
| `resource_constraints.py` | 예제 코드 |
| `scope_constraints.py` | 예제 코드 |
| `step01_example.py` | 예제 코드 |

## 실행 방법

```bash
cd harness-engineering-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-constraint-harness/4.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/harness-engineering-101/ko/04-constraint-harness.md)
