from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import extract_pdf_pages, make_demo_pdf


def main() -> None:
    pdf_path = Path("/tmp/sample_en.pdf")
    make_demo_pdf(
        pdf_path,
        title="Internal wiki PDF",
        author="Platform Team",
        subject="Per-page metadata extraction",
        language="en",
        pages=[
            "This first page explains the deployment flow. Operational documents should store ingestion time and version together with the source text.",
            "This second page describes an incident checklist. Per-page metadata makes citations precise in the UI.",
        ],
    )
    metadata, pages = extract_pdf_pages(pdf_path)

    documents = []
    for page in pages:
        documents.append(
            {
                "text": page["text"],
                "metadata": page["metadata"]
                | {"collection": "ops-wiki", "language": "en"},
            }
        )

    print("Per-page records ready for a document loader")
    print(f"PDF metadata: {metadata}")
    print()
    for record in documents:
        print(record)


if __name__ == "__main__":
    main()
