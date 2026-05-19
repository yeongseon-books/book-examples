# llm-api-production-101

Groq 기반 LLM API 프로덕션 패턴 예제를 `ko/` + `en/` 이중 구조로 정리한 저장소입니다.

## Repository layout

```text
.
├── ko/
│   ├── 01-structured-output/
│   ├── 02-tool-calling/
│   ├── 03-streaming-in-depth/
│   ├── 04-caching-strategies/
│   ├── 05-retry-and-error-handling/
│   └── 06-rate-limit-management/
└── en/
    ├── 01-structured-output/
    ├── 02-tool-calling/
    ├── 03-streaming-in-depth/
    ├── 04-caching-strategies/
    ├── 05-retry-and-error-handling/
    └── 06-rate-limit-management/
```

## Series map

| Topic | Korean | English |
|---|---|---|
| Structured output | `ko/01-structured-output/` | `en/01-structured-output/` |
| Tool calling | `ko/02-tool-calling/` | `en/02-tool-calling/` |
| Streaming in depth | `ko/03-streaming-in-depth/` | `en/03-streaming-in-depth/` |
| Caching strategies | `ko/04-caching-strategies/` | `en/04-caching-strategies/` |
| Retry and error handling | `ko/05-retry-and-error-handling/` | `en/05-retry-and-error-handling/` |
| Rate limit management | `ko/06-rate-limit-management/` | `en/06-rate-limit-management/` |

## Environment

- Python 3.10+
- `GROQ_API_KEY` environment variable
- Model: `llama-3.1-8b-instant`

## Quick start

```bash
git clone https://github.com/yeongseon-books/llm-api-production-101.git
cd llm-api-production-101

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export GROQ_API_KEY="your-key"
python3 ko/01-structured-output/step01_json_mode.py
python3 en/01-structured-output/step01_json_mode.py
```

## Notes

- `ko/` keeps every user-facing string in Korean.
- `en/` keeps the same logic with English strings.
- Tool loop examples manually build the assistant tool-call entry and do not use `model_dump()`.
