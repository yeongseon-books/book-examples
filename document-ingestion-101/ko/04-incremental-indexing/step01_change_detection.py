from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import JsonStateStore, incremental_scan, write_text


def main() -> None:
    workspace = Path("/tmp/document_ingestion_ko_change_detection")
    doc_a = write_text(workspace / "guide.txt", "첫 번째 버전의 가이드 문서")
    doc_b = write_text(workspace / "runbook.txt", "운영 런북 초안")
    store = JsonStateStore(workspace / "state.json")

    first_pass = incremental_scan([doc_a, doc_b], store)
    write_text(doc_b, "운영 런북 초안\n장애 대응 절차 추가")
    second_pass = incremental_scan([doc_a, doc_b], store)

    print("첫 번째 스캔")
    for change in first_pass:
        print(change)

    print()
    print("두 번째 스캔")
    for change in second_pass:
        print(change)


if __name__ == "__main__":
    main()
