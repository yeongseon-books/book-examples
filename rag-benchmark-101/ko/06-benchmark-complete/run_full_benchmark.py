from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.rag_pipeline import run_pipeline_benchmark
from ko.shared import CORPUS, FULL_CONFIGS, PIPELINE_CASES


def main() -> None:
    print("완전한 RAG 벤치마크 실행")
    results = [
        run_pipeline_benchmark("ko", CORPUS, PIPELINE_CASES, config).summary()
        for config in FULL_CONFIGS
    ]
    results.sort(key=lambda row: row["overall_score"], reverse=True)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
