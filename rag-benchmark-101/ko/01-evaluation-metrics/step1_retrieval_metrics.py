from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.retrieval import compute_retrieval_metrics


def main() -> None:
    retrieved = ["d02", "d03", "d08", "d01", "d09"]
    relevant = {"d02", "d03"}
    print("검색 평가 지표 데모")
    for k in (1, 3, 5):
        metrics = compute_retrieval_metrics(retrieved, relevant, k)
        print(f"K={k}")
        print(json.dumps(metrics.summary(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
