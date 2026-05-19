from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from en.shared import CORPUS, QUERIES


def main() -> None:
    print("Test corpus")
    print(json.dumps(CORPUS, indent=2))
    print("\nQuery and ground-truth set")
    rows = [{"query": item.query, "relevant_ids": sorted(item.relevant_ids), "topic": item.topic} for item in QUERIES]
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
