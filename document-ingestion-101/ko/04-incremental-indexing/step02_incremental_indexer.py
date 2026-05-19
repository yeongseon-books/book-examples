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
    search_faiss,
    write_text,
)


def main() -> None:
    workspace = Path("/tmp/document_ingestion_ko_indexer")
    store = JsonStateStore(workspace / "state.json")
    doc_a = write_text(
        workspace / "guide.txt", "문서 수집 가이드: PDF 파싱과 메타데이터 설계"
    )
    doc_b = write_text(workspace / "ops.txt", "운영 문서: 증분 인덱싱과 변경 감지")

    changes = incremental_scan([doc_a, doc_b], store)
    changed_records = [
        {
            "text": change["path"].read_text(encoding="utf-8"),
            "metadata": {"source": str(change["path"]), "status": change["status"]},
        }
        for change in changes
    ]
    index, items = build_faiss_index(changed_records)
    hits = search_faiss(index, items, "변경 감지 인덱싱", top_k=2)

    print("이번 배치에서 다시 인덱싱한 문서")
    for change in changes:
        print(f"- {change['path'].name}: {change['status']}")

    print()
    print("검색 결과")
    for hit in hits:
        print(f"score={hit.score:.4f} source={hit.metadata['metadata']['source']}")
        print(hit.metadata["text"])


if __name__ == "__main__":
    main()
