# langchain-101

Step-by-step LangChain examples for the `langchain-101` series.

## Structure

- `ko/`: Korean prompts, print messages, and corpora
- `en/`: English prompts, print messages, and corpora

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GROQ_API_KEY="your_groq_api_key"
```

## Examples

### 01-lcel-runnable-basics
- `step01_basic_chain.py`: prompt | llm | parser
- `step02_runnable_map.py`: RunnableMap with parallel inputs

### 02-prompt-llm-chain
- `step01_str_output_and_passthrough.py`: StrOutputParser + RunnablePassthrough
- `step02_json_output_parser.py`: JsonOutputParser

### 03-retriever
- `step01_build_faiss.py`: build a FAISS vector store
- `step02_rag_chain.py`: retrieve context and answer questions

### 04-tool-calling
- `step01_basic_tools.py`: `@tool` + `bind_tools`
- `step02_tool_loop.py`: explicit tool-calling loop

### 05-streaming
- `step01_sync_stream.py`: `chain.stream()`
- `step02_async_stream.py`: `chain.astream()`

### 06-putting-it-together
- `step01_multiturn_rag_app.py`: a complete multi-turn RAG console app

## Run

Examples are mirrored across `ko/` and `en/` with localized user-facing strings.

```bash
python3 ko/01-lcel-runnable-basics/step01_basic_chain.py
python3 en/06-putting-it-together/step01_multiturn_rag_app.py
```
