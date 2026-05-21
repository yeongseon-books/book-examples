"""Generated from book-content article."""

def multiplication_rule(*counts: int) -> int:
    out = 1
    for c in counts:
        out *= c
    return out


def addition_rule(*counts: int) -> int:
    return sum(counts)
