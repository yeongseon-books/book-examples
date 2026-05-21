# LangChain 101 (2/6): Prompt와 LLM Chain — 체인 첫 번째 구성

Langchain 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- ChatPromptTemplate는 단순 문자열 포맷팅과 무엇이 다를까요?
- 여러 입력 변수와 parser를 붙이면 체인의 입출력 모양은 어떻게 바뀔까요?
- fallback은 어떤 실패를 숨기고 어떤 실패는 여전히 드러내야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_str_output_and_passthrough.py` | 예제 코드 |
| `step02_json_output_parser.py` | 예제 코드 |

## 실행 방법

```bash
cd langchain-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-prompt-llm-chain/step01_str_output_and_passthrough.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langchain-101/ko/02-prompt-llm-chain.md)
