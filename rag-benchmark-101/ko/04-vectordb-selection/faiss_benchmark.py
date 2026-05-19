"""Rag Benchmark 101 - Faiss benchmark."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.embeddings import build_embeddings
from common.faiss_utils import build_faiss_index, faiss_search
from common.retrieval import compute_retrieval_metrics
from ko.shared import CORPUS, QUERIES, VECTOR_INDEXES


def main() -> None:
    """Main."""
    print("FAISS 인덱스 비교")
    doc_ids = [doc["id"] for doc in CORPUS]
    doc_vectors = build_embeddings(
        [doc["text"] for doc in CORPUS],
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    )
    query_vectors = build_embeddings(
        [query.query for query in QUERIES],
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    )
    rows = []
    for candidate in VECTOR_INDEXES:
        index = build_faiss_index(doc_vectors, candidate.factory)
        ranked_ids, latency_ms = faiss_search(index, query_vectors, doc_ids, 3)
        metrics = [
            compute_retrieval_metrics(ids, query.relevant_ids, 3)
            for ids, query in zip(ranked_ids, QUERIES, strict=False)
        ]
        rows.append(
            {
                "index": candidate.name,
                "factory": candidate.factory,
                "avg_precision@3": round(
                    sum(item.precision_at_k for item in metrics) / len(metrics), 4
                ),
                "avg_recall@3": round(
                    sum(item.recall_at_k for item in metrics) / len(metrics), 4
                ),
                "avg_mrr": round(sum(item.mrr for item in metrics) / len(metrics), 4),
                "search_latency_ms": round(latency_ms, 4),
            }
        )
    print(json.dumps(rows, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
