from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.rag_pipeline import run_pipeline_benchmark
from en.shared import CORPUS, FULL_CONFIGS, PIPELINE_CASES


def main() -> None:
    print("Running the complete RAG benchmark")
    results = [
        run_pipeline_benchmark("en", CORPUS, PIPELINE_CASES, config).summary()
        for config in FULL_CONFIGS
    ]
    results.sort(key=lambda row: row["overall_score"], reverse=True)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
