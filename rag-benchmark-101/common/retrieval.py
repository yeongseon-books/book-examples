from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable

from common.models import QueryGroundTruth, RetrievalMetrics


def compute_retrieval_metrics(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> RetrievalMetrics:
    top_k = retrieved_ids[:k]
    hits = [doc_id for doc_id in top_k if doc_id in relevant_ids]
    precision = len(hits) / k if k else 0.0
    recall = len(hits) / len(relevant_ids) if relevant_ids else 0.0
    mrr = next((1.0 / rank for rank, doc_id in enumerate(top_k, start=1) if doc_id in relevant_ids), 0.0)
    return RetrievalMetrics(precision_at_k=precision, recall_at_k=recall, mrr=mrr, k=k)


def run_retrieval_benchmark(
    queries: list[QueryGroundTruth],
    search_fn: Callable[[str, int], list[str]],
    k_values: list[int],
) -> dict[str, object]:
    per_query: list[dict[str, Any]] = []
    per_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for case in queries:
        retrieved_ids = search_fn(case.query, max(k_values))
        row: dict[str, Any] = {"query": case.query, "topic": case.topic}
        for k in k_values:
            metrics = compute_retrieval_metrics(retrieved_ids, case.relevant_ids, k)
            row.update(metrics.summary())
        per_query.append(row)
        per_topic[case.topic].append(row)

    def average(rows: list[dict[str, Any]], key: str) -> float:
        values = [float(value) for row in rows if isinstance((value := row.get(key)), (int, float))]
        return round(sum(values) / len(values), 4) if values else 0.0

    keys = [*(f"precision@{k}" for k in k_values), *(f"recall@{k}" for k in k_values), *(f"f1@{k}" for k in k_values), "mrr"]
    summary = {key: average(per_query, key) for key in keys}
    summary["total_queries"] = len(queries)
    topic_summary = {
        topic: {key: average(rows, key) for key in keys}
        for topic, rows in per_topic.items()
    }
    return {"summary": summary, "per_topic": topic_summary, "details": per_query}
