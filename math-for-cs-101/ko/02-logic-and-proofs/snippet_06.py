"""Generated from book-content article."""

from itertools import product


def imply(p: bool, q: bool) -> bool:
    return (not p) or q

def equivalent(f, g):
    rows = []
    for p, q in product([False, True], repeat=2):
        rows.append((p, q, f(p, q), g(p, q), f(p, q) == g(p, q)))
    return rows

rows = equivalent(lambda p, q: imply(p, q), lambda p, q: imply((not q), (not p)))
