from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import make_demo_pdf, route_document, write_csv, write_json, write_text


def prepare_files(base: Path) -> list[Path]:
    txt_path = write_text(base / "guide.txt", "텍스트 문서는 바로 읽을 수 있습니다.")
    md_path = write_text(
        base / "architecture.md",
        "# 수집 파이프라인\n\n## 파싱\nPyMuPDF로 PDF를 읽습니다.\n\n## 청킹\n헤딩 기준으로 나눕니다.\n",
    )
    json_path = write_json(base / "meta.json", [{"source": "handbook", "team": "platform"}])
    csv_path = write_csv(base / "inventory.csv", [{"name": "guide", "owner": "ops"}])
    pdf_path = make_demo_pdf(
        base / "sample.pdf",
        title="다중 포맷 테스트",
        author="yeongseon-books",
        subject="라우터 데모",
        language="ko",
        pages=["PDF도 같은 인터페이스로 라우팅합니다."],
    )
    return [txt_path, md_path, json_path, csv_path, pdf_path]


def main() -> None:
    base = Path("/tmp/document_ingestion_ko_router")
    paths = prepare_files(base)
    for path in paths:
        documents = route_document(path)
        print(f"{path.name} -> {len(documents)}개 레코드")
        for document in documents:
            print(document)
        print()


if __name__ == "__main__":
    main()
