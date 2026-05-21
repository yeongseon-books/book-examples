"""Ai Data Preparation 101 - Episode 3: cleaning deduplication example."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import exact_dedup, jaccard_similarity, normalize_text


def run() -> dict[str, int]:
    """Run."""
    docs = [
        "<p>Data prep is important.</p>",
        "Data prep is important.",
        "Data preparation is very important for model quality.",
    ]
    cleaned = [normalize_text(d) for d in docs]
    exact = exact_dedup(cleaned)
    kept = [exact[0]]
    for doc in exact[1:]:
        if jaccard_similarity(kept[-1], doc) < 0.75:
            kept.append(doc)
    return {"raw": len(docs), "exact": len(exact), "near": len(kept)}


if __name__ == "__main__":
    print(run())
