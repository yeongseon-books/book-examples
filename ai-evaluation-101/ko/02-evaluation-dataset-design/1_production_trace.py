"""Generated from book-content article."""

import random

def sample_from_production(traces: list[dict], n: int = 50) -> list[dict]:
    return random.sample(traces, min(n, len(traces)))
