from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import JsonStateStore, incremental_scan, write_text


def main() -> None:
    workspace = Path("/tmp/document_ingestion_en_change_detection")
    doc_a = write_text(workspace / "guide.txt", "The first version of the guide")
    doc_b = write_text(workspace / "runbook.txt", "Operations runbook draft")
    store = JsonStateStore(workspace / "state.json")

    first_pass = incremental_scan([doc_a, doc_b], store)
    write_text(doc_b, "Operations runbook draft\nAdded incident response steps")
    second_pass = incremental_scan([doc_a, doc_b], store)

    print("First scan")
    for change in first_pass:
        print(change)

    print()
    print("Second scan")
    for change in second_pass:
        print(change)


if __name__ == "__main__":
    main()
