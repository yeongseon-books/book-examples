"""Ai Data Preparation 101 - Episode 2: source data collection cataloging example."""

import hashlib
import json


def run() -> dict[str, str | int]:
    """Run."""
    rows = ["hello,world", "data,prep", "catalog,entry"]
    payload = "\n".join(rows).encode("utf-8")
    return {
        "name": "mock-corpus",
        "version": "1.0.0",
        "row_count": len(rows),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
