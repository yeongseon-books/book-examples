from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.models import BenchmarkConfig
from common.rag_pipeline import result_to_json, run_pipeline_benchmark
from en.shared import CORPUS, PIPELINE_CASES


def main() -> None:
    print("Running end-to-end evaluation")
    config = BenchmarkConfig(
        name="e2e-en",
        embedding_model="sentence-transformers/all-MiniLM-L6-v2",
        top_k=3,
        answer_prompt="Answer the question using only the context below. If the answer is missing, say so clearly.\n\nContext:\n{context}\n\nQuestion:\n{question}",
    )
    result = run_pipeline_benchmark("en", CORPUS, PIPELINE_CASES, config)
    print(result_to_json(result))


if __name__ == "__main__":
    main()
