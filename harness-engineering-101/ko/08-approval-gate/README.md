# Harness Engineering 101 (8/10): Approval Gate — 사람 승인이 필요한 지점 설계하기

Harness Engineering 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- Approval Gate는 자동화를 멈추는 방해물이 아니라 어떤 결정 권한을 구조화할까요?
- 어떤 행동은 dry-run으로 충분하고 어떤 행동은 사람 승인이 필요할까요?
- 승인 로그에는 나중에 무엇을 재구성할 수 있도록 남겨야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `approval_gate.py` | 예제 코드 |
| `approval_gate_02.py` | 예제 코드 |
| `approval_workflow.py` | 예제 코드 |
| `decision_logging.py` | 예제 코드 |
| `dry_run_vs_commit.py` | 예제 코드 |
| `step01_example.py` | 예제 코드 |
| `timeout.py` | 예제 코드 |

## 실행 방법

```bash
cd harness-engineering-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-approval-gate/approval_gate.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/harness-engineering-101/ko/08-approval-gate.md)
