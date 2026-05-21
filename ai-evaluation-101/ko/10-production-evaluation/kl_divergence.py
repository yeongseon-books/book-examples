"""Generated from book-content article."""

import math
from collections import Counter

def kl_divergence(p: dict[str, float], q: dict[str, float], eps: float = 1e-9) -> float:
    """KL(P || Q): how much P diverges from Q."""
    total = 0.0
    for key, p_val in p.items():
        q_val = q.get(key, eps)
        total += p_val * math.log((p_val + eps) / (q_val + eps))
    return total

def category_distribution(traces: list[dict]) -> dict[str, float]:
    counts = Counter(t["category"] for t in traces)
    n = sum(counts.values())
    return {k: v / n for k, v in counts.items()}

baseline = category_distribution(traces_last_week)
current = category_distribution(traces_today)
drift = kl_divergence(current, baseline)

if drift > 0.1:
    alert("Input distribution drift detected")
