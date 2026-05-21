# AI Agent 101 (4/10): Agent Workflow 설계

Ai Agent 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- agent workflow를 고를 때 prompt 튜닝보다 먼저 그려야 할 흐름은 무엇일까요?
- ReAct, Plan-and-Execute, Reflexion은 각각 어떤 실패 조건에서 유리할까요?
- workflow 안에서 state와 검증 단계를 어디에 두어야 운영이 쉬워질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `plan_and_execute.py` | 예제 코드 |
| `react.py` | 예제 코드 |
| `reflexion.py` | 예제 코드 |
| `step01_workflow_patterns.py` | 예제 코드 |
| `workflow.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-agent-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-agent-workflow-design/plan_and_execute.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-agent-101/ko/04-agent-workflow-design.md)
