"""Document Ingestion 101 - Episode 1: Metadata schema."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def build_chunks() -> list[dict[str, object]]:
    """Build chunks."""
    return [
        {
            "text": "The PDF parser extracts text page by page.",
            "metadata": {
                "source": "handbook.pdf",
                "page": 1,
                "section": "pdf-parsing",
                "doc_type": "guide",
                "team": "platform",
                "language": "en",
            },
        },
        {
            "text": "The incremental indexer only reprocesses changed files.",
            "metadata": {
                "source": "runbook.pdf",
                "page": 4,
                "section": "incremental-indexing",
                "doc_type": "runbook",
                "team": "ops",
                "language": "en",
            },
        },
    ]


def main() -> None:
    """Main."""
    print("Chunk metadata schema example")
    for chunk in build_chunks():
        print(chunk)


if __name__ == "__main__":
    main()
