from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import JsonStateStore, build_faiss_index, incremental_scan, search_faiss, write_text


def main() -> None:
    workspace = Path("/tmp/document_ingestion_en_indexer")
    store = JsonStateStore(workspace / "state.json")
    doc_a = write_text(workspace / "guide.txt", "Ingestion guide: PDF parsing and metadata design")
    doc_b = write_text(workspace / "ops.txt", "Operations notes: incremental indexing and change detection")

    changes = incremental_scan([doc_a, doc_b], store)
    changed_records = [
        {"text": change["path"].read_text(encoding="utf-8"), "metadata": {"source": str(change["path"]), "status": change["status"]}}
        for change in changes
    ]
    index, items = build_faiss_index(changed_records)
    hits = search_faiss(index, items, "change detection indexing", top_k=2)

    print("Documents re-indexed in this batch")
    for change in changes:
        print(f"- {change['path'].name}: {change['status']}")

    print()
    print("Search results")
    for hit in hits:
        print(f"score={hit.score:.4f} source={hit.metadata['metadata']['source']}")
        print(hit.metadata["text"])


if __name__ == "__main__":
    main()
