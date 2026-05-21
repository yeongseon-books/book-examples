# LangGraph 101 (4/6): 도구 호출 에이전트

Langgraph 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- LangGraph tool-calling agent는 왜 LLM과 tool 실행 envelope를 분리해서 봐야 할까요?
- 도구 호출을 반복할 때 state에는 어떤 실행 흔적이 남아야 할까요?
- 안전한 dispatcher 없이 tool call을 실행하면 어떤 위험이 생길까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_toolnode_with_chatgroq.py` | 예제 코드 |
| `step02_agent_loop.py` | 예제 코드 |

## 실행 방법

```bash
cd langgraph-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-tool-calling-agent/step01_toolnode_with_chatgroq.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langgraph-101/ko/04-tool-calling-agent.md)
