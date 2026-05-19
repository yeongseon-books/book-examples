# vector-search-101

Runnable example code for the `vector-search-101` series, rebuilt into parallel Korean and English tracks.

`vector-search-101` 시리즈의 예제 코드 저장소입니다.

## Repository layout

```text
vector-search-101/
├── .gitignore
├── README.md
├── requirements.txt
├── ko/
│   ├── 01-what-is-embedding/step01_first_vector.py
│   ├── 02-huggingface-embeddings/step01_batch_embeddings.py
│   ├── 03-cosine-similarity/step01_distance_metrics.py
│   ├── 04-faiss-fundamentals/step01_indexflat_search.py
│   ├── 05-chunking-strategies/step01_chunking_and_search.py
│   └── 06-vector-search-pipeline/step01_pipeline.py
└── en/
    ├── 01-what-is-embedding/step01_first_vector.py
    ├── 02-huggingface-embeddings/step01_batch_embeddings.py
    ├── 03-cosine-similarity/step01_distance_metrics.py
    ├── 04-faiss-fundamentals/step01_indexflat_search.py
    ├── 05-chunking-strategies/step01_chunking_and_search.py
    └── 06-vector-search-pipeline/step01_pipeline.py
```

## Series steps

| Step | Topic |
|---|---|
| `01-what-is-embedding` | First embedding vector |
| `02-huggingface-embeddings` | Batch embeddings and cosine similarity |
| `03-cosine-similarity` | Comparing distance metrics |
| `04-faiss-fundamentals` | FAISS `IndexFlatIP` search |
| `05-chunking-strategies` | Fixed-size chunking and retrieval |
| `06-vector-search-pipeline` | End-to-end vector search pipeline |

## Environment

- Python 3.10+
- Model: `sentence-transformers/all-MiniLM-L6-v2`
- CPU-only execution is supported
- No external API call is required

## Setup

```bash
git clone https://github.com/yeongseon-books/vector-search-101.git
cd vector-search-101

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run examples

```bash
python3 ko/01-what-is-embedding/step01_first_vector.py
python3 en/01-what-is-embedding/step01_first_vector.py
python3 -m py_compile $(find ko en -name '*.py')
```

## Packages

| Package | Version |
|---|---|
| sentence-transformers | 5.4.1 |
| faiss-cpu | 1.11.0 |
| numpy | 2.3.0 |
