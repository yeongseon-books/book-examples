# LangChain 101 (4/6): Tool Calling — 외부 도구 연결하기

Langchain 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- `bind_tools()`는 모델에게 실행 권한을 주는 걸까요, 호출 형식을 정의하는 걸까요?
- tool call을 실제 함수 실행으로 연결하기 전에 무엇을 검증해야 할까요?
- 여러 도구를 섞을 때 dispatcher는 어떤 실패를 막아야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_basic_tools.py` | 예제 코드 |
| `step02_tool_loop.py` | 예제 코드 |

## 실행 방법

```bash
cd langchain-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-tool-calling/step01_basic_tools.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langchain-101/ko/04-tool-calling.md)
