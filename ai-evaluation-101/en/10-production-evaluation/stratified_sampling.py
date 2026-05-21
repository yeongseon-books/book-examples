"""Generated from book-content article."""

from collections import defaultdict


def stratified_sample(traces: list[dict], per_category: int = 50) -> list[dict]:
    buckets = defaultdict(list)
    for t in traces:
        buckets[t["category"]].append(t)
    sampled = []
    for _cat, items in buckets.items():
        n = min(per_category, len(items))
        sampled.extend(random.sample(items, n))
    return sampled
