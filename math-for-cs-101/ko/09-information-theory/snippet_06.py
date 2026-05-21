"""Generated from book-content article."""

import math


def entropy(probs: list[float]) -> float:
    return -sum(p * math.log2(p) for p in probs if p > 0)

fair_coin = [0.5, 0.5]
biased_coin = [0.9, 0.1]

h_fair = entropy(fair_coin)
h_biased = entropy(biased_coin)
