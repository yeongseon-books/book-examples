# AI App Patterns 101 (4/6): 에이전트와 도구 패턴 — 자율적 도구 선택

Ai App Patterns 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- 에이전트가 “도구를 고른다”는 말은 실제로 어디까지 자율적이라는 뜻일까요?
- 도구 실행 전에 이름과 인자를 검증하지 않으면 어떤 위험이 생길까요?
- ReAct 로그를 보면 에이전트 실패를 어떻게 더 빨리 좁힐 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_manual_tool_loop.py` | 예제 코드 |
| `step02_safe_tool_retry.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-app-patterns-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-agent-tool-pattern/step01_manual_tool_loop.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-app-patterns-101/ko/04-agent-tool-pattern.md)
