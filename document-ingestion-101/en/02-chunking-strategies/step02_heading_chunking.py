from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import heading_chunks

MARKDOWN = """# Document ingestion design

The introduction explains the goal of the system.

## PDF parsing

PyMuPDF exposes per-page text and metadata.

## Chunking strategy

Fixed-size chunking is simple and fast.
Recursive chunking preserves semantic boundaries more reliably.

## Incremental indexing

Store file hashes so only changed files are reprocessed.
"""


def main() -> None:
    chunks = heading_chunks(MARKDOWN)
    print("Heading-aware chunks")
    for chunk in chunks:
        print(f"- heading={chunk['heading']}, slug={chunk['slug']}")
        print(chunk["text"])
        print()


if __name__ == "__main__":
    main()
