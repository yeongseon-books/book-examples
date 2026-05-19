from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import (
    JsonStateStore,
    build_faiss_index,
    incremental_scan,
    make_demo_pdf,
    route_document,
    search_faiss,
    write_text,
)


def prepare_sources(base: Path) -> list[Path]:
    txt_path = write_text(
        base / "handbook.txt",
        "A document ingestion pipeline has a parser, a chunker, an indexer, and a state store.",
    )
    md_path = write_text(
        base / "ops.md",
        "# Operations notes\n\n## Change detection\nCompare file hashes.\n\n## Reprocessing\nOnly re-embed changed files.\n",
    )
    pdf_path = make_demo_pdf(
        base / "reference.pdf",
        title="Document ingestion reference",
        author="yeongseon-books",
        subject="Unified pipeline",
        language="en",
        pages=[
            "PDF parsing should preserve page-level metadata.",
            "Search results should show the page number and source file name.",
        ],
    )
    return [txt_path, md_path, pdf_path]


def main() -> None:
    base = Path("/tmp/document_ingestion_en_complete")
    store = JsonStateStore(base / "state.json")
    sources = prepare_sources(base)
    changes = incremental_scan(sources, store)

    records = []
    for change in changes:
        for document in route_document(change["path"]):
            document["metadata"] = document["metadata"] | {
                "change_status": change["status"]
            }
            records.append(document)

    index, items = build_faiss_index(records)
    hits = search_faiss(index, items, "page metadata and change detection", top_k=3)

    print("Ingested files")
    for change in changes:
        print(f"- {change['path'].name}: {change['status']}")

    print()
    print("Search results")
    for hit in hits:
        metadata = hit.metadata["metadata"]
        print(
            f"score={hit.score:.4f} source={metadata['source']} format={metadata.get('format', 'txt')}"
        )
        print(hit.metadata["text"])
        print()


if __name__ == "__main__":
    main()
