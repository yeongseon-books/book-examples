"""Document Ingestion 101 - Episode 2: Incremental indexer."""

from __future__ import annotations

import json
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
    """Main."""
    workspace = Path("/tmp/document_ingestion_ko_indexer")
    store = JsonStateStore(workspace / "state.json")
    doc_a = write_text(
        workspace / "guide.txt", "문서 수집 가이드: PDF 파싱과 메타데이터 설계"
    )
    doc_b = write_text(workspace / "ops.txt", "운영 문서: 증분 인덱싱과 변경 감지")

    changes = incremental_scan([doc_a, doc_b], store)
    records_path = workspace / "index_items.json"
    existing_records = (
        json.loads(records_path.read_text(encoding="utf-8"))
        if records_path.exists()
        else []
    )
    changed_records = [
        {
            "text": change["path"].read_text(encoding="utf-8"),
            "metadata": {"source": str(change["path"]), "status": change["status"]},
        }
        for change in changes
    ]
    items = [*existing_records, *changed_records]
    records_path.parent.mkdir(parents=True, exist_ok=True)
    records_path.write_text(
        json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if items:
        index, items = build_faiss_index(items)
        hits = search_faiss(index, items, "변경 감지 인덱싱", top_k=2)
    else:
        hits = []

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
