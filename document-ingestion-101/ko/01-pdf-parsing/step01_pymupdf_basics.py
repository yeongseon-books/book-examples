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
    pdf_path = Path("/tmp/sample_ko.pdf")
    make_demo_pdf(
        pdf_path,
        title="문서 수집 파이프라인",
        author="yeongseon-books",
        subject="PyMuPDF 기본 파싱 예제",
        language="ko",
        pages=[
            "첫 번째 페이지입니다. PDF 안에서 텍스트를 꺼낼 때는 페이지 번호와 원본 경로를 같이 남겨야 나중에 검색 결과를 설명하기 쉽습니다.",
            "두 번째 페이지입니다. 문단 경계와 제목을 함께 보존하면 청킹 이후에도 문맥을 다시 복원하기가 수월합니다.",
        ],
    )
    metadata, pages = extract_pdf_pages(pdf_path)

    print(f"생성된 PDF: {pdf_path}")
    print(f"제목: {metadata.get('title')}")
    print(f"작성자: {metadata.get('author')}")
    print(f"주제: {metadata.get('subject')}")
    print()
    for page in pages:
        print(f"[페이지 {page['page']}] {page['text']}")
        print(f"메타데이터: {page['metadata']}")
        print()


if __name__ == "__main__":
    main()
