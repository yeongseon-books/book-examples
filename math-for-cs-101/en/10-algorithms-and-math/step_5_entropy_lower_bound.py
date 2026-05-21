"""Generated from book-content article."""

import math


def lower_bound_bits(probs):
    return sum(-p * math.log2(p) for p in probs if p > 0)
