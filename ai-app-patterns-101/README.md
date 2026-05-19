# ai-app-patterns-101

Example code for the AI App Patterns 101 series.

## Requirements

- Python 3.11+
- `GROQ_API_KEY` environment variable

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run examples

Korean examples live under `ko/` and English examples live under `en/`.

```bash
python3 ko/01-chatbot-pattern/step01_session_chatbot.py
python3 en/02-rag-qa-pattern/step02_rag_with_sources.py
```

## Directory map

- `01-chatbot-pattern` — session memory and summary compression
- `02-rag-qa-pattern` — retrieval + grounded answers with sources
- `03-document-assistant` — summarization, extraction, classification
- `04-agent-tool-pattern` — ReAct-style tool loop and safe retries
- `05-workflow-automation` — sequential chains and routing workflows
- `06-human-in-the-loop` — approval gates and confidence branching

## Notes

- All examples use the Groq SDK directly with `from groq import Groq`.
- Tool call messages are appended with manual dictionaries, not `model_dump()`.
- The examples are intentionally small and readable for blog readers.
