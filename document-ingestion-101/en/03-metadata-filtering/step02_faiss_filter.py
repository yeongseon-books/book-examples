from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import build_faiss_index, search_faiss


def main() -> None:
    records = [
        {
            "text": "The PDF parser stores page numbers and titles together with text.",
            "metadata": {"team": "platform", "doc_type": "guide", "language": "en"},
        },
        {
            "text": "The operations runbook contains incident response steps.",
            "metadata": {"team": "ops", "doc_type": "runbook", "language": "en"},
        },
        {
            "text": "Chunking strategy directly affects retrieval quality.",
            "metadata": {"team": "platform", "doc_type": "guide", "language": "en"},
        },
    ]
    index, items = build_faiss_index(records)
    hits = search_faiss(
        index, items, "chunking and PDF parsing", top_k=2, filters={"team": "platform"}
    )

    print("Search results filtered to platform team documents")
    for hit in hits:
        print(f"score={hit.score:.4f} text={hit.metadata['text']}")
        print(f"metadata={hit.metadata['metadata']}")


if __name__ == "__main__":
    main()
