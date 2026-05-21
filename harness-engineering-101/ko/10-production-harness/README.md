# Harness Engineering 101 (10/10): Production Harness — 운영 가능한 Agent 작업 환경 만들기

Harness Engineering 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- Production Harness는 여러 harness를 어떻게 하나의 배포 가능한 운영 스택으로 묶을까요?
- 점진적 rollout과 rollback은 agent 시스템에서 왜 설계의 일부여야 할까요?
- 새벽 장애를 견디려면 runbook에는 어떤 실행 정보가 있어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `9_harness.py` | 예제 코드 |
| `capstone_example.py` | 예제 코드 |
| `deployment_pattern.py` | 예제 코드 |
| `production_harness.py` | 예제 코드 |
| `rollback.py` | 예제 코드 |
| `step01_example.py` | 예제 코드 |

## 실행 방법

```bash
cd harness-engineering-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-production-harness/9_harness.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/harness-engineering-101/ko/10-production-harness.md)
