"""Generated from book-content article."""

import random


def uniform_sample(traces: list[dict], rate: float = 0.01) -> list[dict]:
    """Pick `rate` fraction of traces uniformly."""
    return [t for t in traces if random.random() < rate]

# 1% of 100k daily requests = 1,000 traces for evaluation
sampled = uniform_sample(today_traces, rate=0.01)
