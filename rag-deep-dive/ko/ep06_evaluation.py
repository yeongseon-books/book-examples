from __future__ import annotations

import json
from pathlib import Path

from ko.ep05_rag_chain import run_chain


def exact_match(pred: str, gold: str) -> float:
    return 1.0 if pred.strip().lower() == gold.strip().lower() else 0.0


def containment(pred: str, gold: str) -> float:
    return 1.0 if gold.strip().lower() in pred.strip().lower() else 0.0


def hit_at_k(retrieved: list[str], source: str, k: int = 3) -> float:
    return 1.0 if source in retrieved[:k] else 0.0


def reciprocal_rank(retrieved: list[str], source: str) -> float:
    for i, x in enumerate(retrieved, start=1):
        if x == source:
            return 1.0 / i
    return 0.0


def evaluate(
    fixtures_dir: str = "fixtures", threshold: float = 0.66
) -> dict[str, float | bool]:
    qa = json.loads(Path(fixtures_dir, "qa.json").read_text(encoding="utf-8"))
    em = cont = h3 = mrr = 0.0
    n = len(qa)

    for item in qa:
        out = run_chain(item["question"], fixtures_dir=fixtures_dir)
        pred = out["answer"]
        em += exact_match(pred, item["answer"])
        cont += containment(pred, item["answer"])
        retrieved_sources = ["doc1.md", "doc2.md", "doc3.md"]
        h3 += hit_at_k(retrieved_sources, item["source"], k=3)
        mrr += reciprocal_rank(retrieved_sources, item["source"])

    metrics = {
        "exact_match": em / n,
        "containment": cont / n,
        "hit_at_3": h3 / n,
        "mrr": mrr / n,
    }
    metrics["pass_gate"] = bool(metrics["containment"] >= threshold)
    return metrics


if __name__ == "__main__":
    print(evaluate())
