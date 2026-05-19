# llm-app-foundations-101

LLM app foundations example repository with parallel Korean and English tracks.
한국어 학습용 예제와 영어 학습용 예제가 같은 구조로 들어 있습니다.

`llm-app-foundations-101` 시리즈의 예제 코드 저장소입니다.

## Repository layout

```text
llm-app-foundations-101/
├── ko/
│   ├── 01-llm-api-first-call/
│   ├── 02-understanding-tokens/
│   ├── 03-prompt-engineering-basics/
│   ├── 04-few-shot-and-cot/
│   ├── 05-conversation-state/
│   └── 06-streaming-responses/
└── en/
    ├── 01-llm-api-first-call/
    ├── 02-understanding-tokens/
    ├── 03-prompt-engineering-basics/
    ├── 04-few-shot-and-cot/
    ├── 05-conversation-state/
    └── 06-streaming-responses/
```

- `ko/`: Korean output, Korean prompts, Korean guidance messages
- `en/`: English output, English prompts, English guidance messages
- Both trees keep the same lesson order and file names so you can compare them side by side.

## Series map

| Directory | Topic |
|---|---|
| `01-llm-api-first-call/` | First LLM API call |
| `02-understanding-tokens/` | Tokens, limits, and usage |
| `03-prompt-engineering-basics/` | Prompt engineering basics |
| `04-few-shot-and-cot/` | Few-shot prompting and Chain-of-Thought |
| `05-conversation-state/` | Conversation state management |
| `06-streaming-responses/` | Streaming responses |

## Environment

- Python 3.10+
- Groq API key ([console.groq.com](https://console.groq.com))
- Model: `llama-3.1-8b-instant`

## Setup

```bash
git clone https://github.com/yeongseon-books/llm-app-foundations-101.git
cd llm-app-foundations-101

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

export GROQ_API_KEY="your-api-key"
```

## Run examples

Each file is standalone.
각 파일은 해당 디렉토리 안에서 바로 실행할 수 있습니다.

```bash
cd ko/01-llm-api-first-call
python step01_check_env.py
python step02_first_call.py
python step03_inspect_response.py
python step04_sync_vs_async.py
python step05_complete_example.py
```

```bash
cd en/01-llm-api-first-call
python step01_check_env.py
python step02_first_call.py
python step03_inspect_response.py
python step04_sync_vs_async.py
python step05_complete_example.py
```

## FastAPI streaming example

```bash
cd en/06-streaming-responses
uvicorn step06_fastapi_stream:app --reload

# or
cd ko/06-streaming-responses
uvicorn step06_fastapi_stream:app --reload
```

Then test with:

```bash
curl "http://localhost:8000/chat/stream?prompt=hello"
```

## Package versions

| Package | Version |
|---|---|
| groq | 1.2.0 |
| tiktoken | 0.12.0 |
| fastapi | 0.136.1 |
| uvicorn | 0.46.0 |
