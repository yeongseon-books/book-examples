"""Rag Benchmark 101 - Episode 2: Run benchmark."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.embeddings import build_embeddings, cosine_ranking
from common.retrieval import run_retrieval_benchmark
from ko.shared import CORPUS, QUERIES


def main() -> None:
    """Main."""
    print("검색 벤치마크 실행")
    doc_ids = [doc["id"] for doc in CORPUS]
    doc_texts = [doc["text"] for doc in CORPUS]
    doc_vectors = build_embeddings(
        doc_texts, "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    def search(query: str, limit: int) -> list[str]:
        """Search."""
        query_vector = build_embeddings(
            [query], "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )[0]
        return cosine_ranking(query_vector, doc_vectors, doc_ids, limit)

    result = run_retrieval_benchmark(QUERIES, search, [1, 3, 5])
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
