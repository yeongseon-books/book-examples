# AI Agent 101 (3/10): Tool Use 기초

Ai Agent 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- function calling에서 모델이 결정하는 일과 애플리케이션 코드가 실행하는 일은 어디서 갈라질까요?
- tool schema가 애매하면 agent는 어떤 방식으로 잘못 실패할까요?
- tool 결과를 다시 모델에게 넣기 전에 무엇을 검증해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_tool_dispatch.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-agent-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-tool-use-fundamentals/step01_tool_dispatch.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-agent-101/ko/03-tool-use-fundamentals.md)
