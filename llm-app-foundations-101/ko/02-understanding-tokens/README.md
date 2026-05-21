# LLM App Foundations 101 (2/6): 토큰 이해하기 — 비용, 한계, 컨텍스트 창

Llm App Foundations 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- 토큰은 단어가 아니라 왜 예산 단위로 봐야 할까요?
- `prompt_tokens`, `completion_tokens`, `total_tokens`는 각각 어떤 비용을 보여 줄까요?
- context window와 `max_tokens`, `finish_reason`은 어디서 충돌할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_read_usage.py` | 예제 코드 |
| `step02_tiktoken_estimate.py` | 예제 코드 |
| `step03_max_tokens.py` | 예제 코드 |
| `step04_long_prompt_guard.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-app-foundations-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-understanding-tokens/step01_read_usage.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-app-foundations-101/ko/02-understanding-tokens.md)
