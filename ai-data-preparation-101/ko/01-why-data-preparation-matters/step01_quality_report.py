"""Ai Data Preparation 101 - 1편: why data preparation matters 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import mock_documents


def run() -> dict[str, float]:
    """Run."""
    docs = mock_documents()
    texts = [d["text"] for d in docs]
    unique_ratio = len(set(texts)) / len(texts)
    avg_len = sum(len(t) for t in texts) / len(texts)
    return {
        "total": float(len(texts)),
        "unique_ratio": unique_ratio,
        "avg_len": avg_len,
    }


if __name__ == "__main__":
    print(run())
