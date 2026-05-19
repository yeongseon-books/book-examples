from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import extract_pdf_pages, make_demo_pdf


def main() -> None:
    pdf_path = Path("/tmp/sample_ko.pdf")
    make_demo_pdf(
        pdf_path,
        title="사내 위키 PDF",
        author="플랫폼 팀",
        subject="페이지 메타데이터 추출",
        language="ko",
        pages=[
            "배포 절차를 설명하는 첫 페이지입니다. 운영 문서는 최신성 확인이 중요하므로 수집 시점과 버전을 같이 저장해야 합니다.",
            "장애 대응 체크리스트를 설명하는 두 번째 페이지입니다. 페이지 단위 메타데이터가 있으면 인용 위치를 정확히 보여줄 수 있습니다.",
        ],
    )
    metadata, pages = extract_pdf_pages(pdf_path)

    documents = []
    for page in pages:
        documents.append(
            {
                "text": page["text"],
                "metadata": page["metadata"]
                | {"collection": "ops-wiki", "language": "ko"},
            }
        )

    print("문서 로더에 넘길 페이지별 레코드")
    print(f"PDF 메타데이터: {metadata}")
    print()
    for record in documents:
        print(record)


if __name__ == "__main__":
    main()
