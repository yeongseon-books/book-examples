# Harness Engineering 101 (6/10): Test Harness — 완료 조건을 테스트로 고정하기

Harness Engineering 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- Test Harness는 완료 조건을 자연어 약속에서 무엇으로 바꿔야 할까요?
- unit, trajectory, end-to-end 테스트는 각각 어떤 agent 실패를 잡을까요?
- eval dataset과 regression check는 운영 전에 어떻게 연결되어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `agent-tests.yml` | 예제 코드 |
| `agent_3.py` | 예제 코드 |
| `eval_dataset.py` | 예제 코드 |
| `rubric.py` | 예제 코드 |
| `snapshot_testing.py` | 예제 코드 |
| `step01_example.py` | 예제 코드 |

## 실행 방법

```bash
cd harness-engineering-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-test-harness/agent_3.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/harness-engineering-101/ko/06-test-harness.md)
