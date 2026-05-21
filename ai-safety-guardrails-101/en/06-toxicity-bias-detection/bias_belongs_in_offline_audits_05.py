"""Generated from book-content article."""

from statistics import mean

def length_gap(responses: dict) -> float:
    means = {g: mean(len(r) for r in rs) for g, rs in responses.items()}
    return max(means.values()) - min(means.values())
