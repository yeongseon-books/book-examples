# document-ingestion-101

문서 수집과 인덱싱 101 시리즈용 예제 코드 저장소입니다.

This repository contains runnable examples for the Document Ingestion 101 series.

## Structure

```text
document-ingestion-101/
├── ko/
│   ├── 01-pdf-parsing/
│   ├── 02-chunking-strategies/
│   ├── 03-metadata-filtering/
│   ├── 04-incremental-indexing/
│   ├── 05-multi-format-pipeline/
│   └── 06-pipeline-completion/
├── en/
│   ├── 01-pdf-parsing/
│   ├── 02-chunking-strategies/
│   ├── 03-metadata-filtering/
│   ├── 04-incremental-indexing/
│   ├── 05-multi-format-pipeline/
│   └── 06-pipeline-completion/
└── shared/
```

## Setup

```bash
pip install -r requirements.txt --break-system-packages
```

## Notes

- `ko/` examples use Korean sample text and Korean print messages.
- `en/` examples use English sample text and English print messages.
- PDF examples generate `/tmp/sample_ko.pdf` and `/tmp/sample_en.pdf` directly in code.
- Vector search examples use deterministic local embeddings so they run without external APIs.

## Quick check

```bash
python3 -m py_compile $(find . -name '*.py')
```
