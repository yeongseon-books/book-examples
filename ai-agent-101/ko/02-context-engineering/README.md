# AI Agent 101 (2/10): 컨텍스트 엔지니어링

Ai Agent 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- agent가 엉뚱하게 행동할 때 prompt 문장보다 먼저 어떤 context 경계를 확인해야 할까요?
- system prompt, 대화 기록, tool 설명, 현재 state는 각각 어떤 책임을 나눌까요?
- context가 길어질수록 무엇을 버리고 무엇을 유지할지 어떻게 판단해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `agent.py` | 예제 코드 |
| `agent_02.py` | 예제 코드 |
| `agent_03.py` | 예제 코드 |
| `agent_04.py` | 예제 코드 |
| `few_shot_downstream.py` | 예제 코드 |
| `few_shot_downstream_07.py` | 예제 코드 |
| `step01_context_builder.py` | 예제 코드 |
| `system_prompt.py` | 예제 코드 |
| `tool.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-agent-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-context-engineering/agent.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-agent-101/ko/02-context-engineering.md)
