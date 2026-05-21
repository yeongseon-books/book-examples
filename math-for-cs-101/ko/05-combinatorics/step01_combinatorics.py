"""Math For Cs 101 - 5편: combinatorics 예제."""

import math


def ncr(n, r):
    """Ncr."""
    return math.comb(n, r)


def npr(n, r):
    """Npr."""
    return math.perm(n, r)


def pigeonhole(items, holes):
    """Pigeonhole."""
    return items > holes
