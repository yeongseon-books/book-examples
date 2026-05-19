from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import fixed_chunks, recursive_chunks

TEXT = """A document ingestion pipeline usually has a parser, a chunker, and an indexer.

The parser extracts raw text and metadata from source files. The chunker breaks long documents into searchable units. The indexer stores embeddings together with metadata.

Fixed-size chunking is simple, but it often cuts through sentence boundaries. Recursive chunking tries paragraphs and sentences first, then falls back to smaller units only when necessary."""


def main() -> None:
    fixed = fixed_chunks(TEXT, size=18, overlap=4)
    recursive = recursive_chunks(TEXT, size=18, overlap=4)

    print("Fixed-size chunks")
    for index, chunk in enumerate(fixed, start=1):
        print(f"{index:02d}. {chunk}")

    print()
    print("Recursive chunks")
    for index, chunk in enumerate(recursive, start=1):
        print(f"{index:02d}. {chunk}")


if __name__ == "__main__":
    main()
