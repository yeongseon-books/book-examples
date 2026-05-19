from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.embeddings import build_embeddings, cosine_ranking, timed_embeddings
from common.retrieval import run_retrieval_benchmark
from en.shared import CORPUS, EMBEDDING_MODELS, QUERIES


def main() -> None:
    print("Embedding model comparison")
    rows = []
    doc_ids = [doc["id"] for doc in CORPUS]
    doc_texts = [doc["text"] for doc in CORPUS]
    for candidate in EMBEDDING_MODELS:
        doc_vectors, embed_ms = timed_embeddings(doc_texts, candidate.model_name)

        def search(query: str, limit: int) -> list[str]:
            query_vector = build_embeddings([query], candidate.model_name)[0]
            return cosine_ranking(query_vector, doc_vectors, doc_ids, limit)

        benchmark = run_retrieval_benchmark(QUERIES, search, [3])
        summary = cast(dict[str, Any], benchmark["summary"])
        rows.append({
            "model": candidate.label,
            "model_name": candidate.model_name,
            "embedding_ms": round(embed_ms, 2),
            **summary,
        })
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
