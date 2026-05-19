from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import (
    make_demo_pdf,
    route_document,
    write_csv,
    write_json,
    write_text,
)


def prepare_files(base: Path) -> list[Path]:
    txt_path = write_text(
        base / "guide.txt", "Plain text documents can be loaded directly."
    )
    md_path = write_text(
        base / "architecture.md",
        "# Ingestion pipeline\n\n## Parsing\nRead PDFs with PyMuPDF.\n\n## Chunking\nSplit by headings when structure is available.\n",
    )
    json_path = write_json(
        base / "meta.json", [{"source": "handbook", "team": "platform"}]
    )
    csv_path = write_csv(base / "inventory.csv", [{"name": "guide", "owner": "ops"}])
    pdf_path = make_demo_pdf(
        base / "sample.pdf",
        title="Multi-format test",
        author="yeongseon-books",
        subject="Router demo",
        language="en",
        pages=["PDF goes through the same router interface as the other formats."],
    )
    return [txt_path, md_path, json_path, csv_path, pdf_path]


def main() -> None:
    base = Path("/tmp/document_ingestion_en_router")
    paths = prepare_files(base)
    for path in paths:
        documents = route_document(path)
        print(f"{path.name} -> {len(documents)} record(s)")
        for document in documents:
            print(document)
        print()


if __name__ == "__main__":
    main()
