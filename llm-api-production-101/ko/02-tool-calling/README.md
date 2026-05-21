# LLM API Production 101 (2/6): 툴 호출 — 함수를 모델에 연결하기

Llm Api Production 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- 툴 호출은 모델에게 실행 권한을 넘기는 기능일까요, 애플리케이션이 만든 실행 경계일까요?
- `tools` 정의와 `tool_calls` 응답에서 각각 무엇을 검증해야 할까요?
- 함수 실행 루프를 운영 환경에서 안전하게 끝내려면 어떤 방어선이 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_basic_tool_call.py` | 예제 코드 |
| `step02_tool_loop.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-api-production-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-tool-calling/step01_basic_tool_call.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-api-production-101/ko/02-tool-calling.md)
