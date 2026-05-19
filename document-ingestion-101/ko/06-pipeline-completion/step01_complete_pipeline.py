from __future__ import annotations

from pathlib import Path
import sys

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
    txt_path = write_text(base / "handbook.txt", "문서 수집 파이프라인은 파서, 청커, 인덱서, 상태 저장소로 구성됩니다.")
    md_path = write_text(
        base / "ops.md",
        "# 운영 메모\n\n## 변경 감지\n파일 해시를 비교합니다.\n\n## 재처리\n변경된 파일만 다시 임베딩합니다.\n",
    )
    pdf_path = make_demo_pdf(
        base / "reference.pdf",
        title="문서 수집 참고서",
        author="yeongseon-books",
        subject="통합 파이프라인",
        language="ko",
        pages=[
            "PDF 파싱은 페이지 메타데이터를 남겨야 합니다.",
            "검색 결과에는 페이지 번호와 원본 파일명이 보여야 합니다.",
        ],
    )
    return [txt_path, md_path, pdf_path]


def main() -> None:
    base = Path("/tmp/document_ingestion_ko_complete")
    store = JsonStateStore(base / "state.json")
    sources = prepare_sources(base)
    changes = incremental_scan(sources, store)

    records = []
    for change in changes:
        for document in route_document(change["path"]):
            document["metadata"] = document["metadata"] | {"change_status": change["status"]}
            records.append(document)

    index, items = build_faiss_index(records)
    hits = search_faiss(index, items, "페이지 메타데이터와 변경 감지", top_k=3)

    print("수집 대상 파일")
    for change in changes:
        print(f"- {change['path'].name}: {change['status']}")

    print()
    print("검색 결과")
    for hit in hits:
        metadata = hit.metadata["metadata"]
        print(f"score={hit.score:.4f} source={metadata['source']} format={metadata.get('format', 'txt')}")
        print(hit.metadata["text"])
        print()


if __name__ == "__main__":
    main()
