"""Document Ingestion 101 - Episode 1: Pymupdf basics."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import extract_pdf_pages, make_demo_pdf


def main() -> None:
    """Main."""
    pdf_path = Path("/tmp/sample_en.pdf")
    make_demo_pdf(
        pdf_path,
        title="Document ingestion pipeline",
        author="yeongseon-books",
        subject="PyMuPDF parsing basics",
        language="en",
        pages=[
            "This is the first page. When you extract text from PDF, keep the page number and source path so retrieval results stay explainable.",
            "This is the second page. If you preserve paragraph boundaries and headings, you can rebuild context after chunking.",
        ],
    )
    metadata, pages = extract_pdf_pages(pdf_path)

    print(f"Generated PDF: {pdf_path}")
    print(f"Title: {metadata.get('title')}")
    print(f"Author: {metadata.get('author')}")
    print(f"Subject: {metadata.get('subject')}")
    print()
    for page in pages:
        print(f"[Page {page['page']}] {page['text']}")
        print(f"Metadata: {page['metadata']}")
        print()


if __name__ == "__main__":
    main()
