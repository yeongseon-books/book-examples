# rag-benchmark-101

`rag-benchmark-101` 시리즈의 참조 구현 예제 코드입니다.

## Repository layout

```text
rag-benchmark-101/
├── common/                        # shared evaluation logic
├── ko/                            # Korean corpus, queries, output messages
│   ├── 01-evaluation-metrics/
│   ├── 02-retrieval-benchmarking/
│   ├── 03-embedding-comparison/
│   ├── 04-vectordb-selection/
│   ├── 05-e2e-evaluation/
│   └── 06-benchmark-complete/
└── en/                            # English corpus, queries, output messages
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GROQ_API_KEY="your-key"
```

## Groq model

All LLM-as-judge examples use `llama-3.1-8b-instant` through the Groq API.

## Quick start

```bash
python3 ko/01-evaluation-metrics/step1_retrieval_metrics.py
python3 ko/02-retrieval-benchmarking/step2_run_benchmark.py
python3 en/06-benchmark-complete/run_full_benchmark.py
```
