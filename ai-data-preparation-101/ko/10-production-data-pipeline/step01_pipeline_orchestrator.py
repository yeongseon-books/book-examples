"""Ai Data Preparation 101 - 10편: production data pipeline 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import exact_dedup, mock_documents, normalize_text, redact_pii


def run() -> dict[str, int]:
    """Run."""
    docs = mock_documents()
    stage1 = [normalize_text(d["text"]) for d in docs]
    stage2 = exact_dedup(stage1)
    stage3 = [redact_pii(t) for t in stage2]
    stage4 = [t for t in stage3 if len(t.split()) >= 5]
    return {
        "ingest": len(docs),
        "clean": len(stage1),
        "dedup": len(stage2),
        "pii": len(stage3),
        "quality": len(stage4),
    }


if __name__ == "__main__":
    print(run())
