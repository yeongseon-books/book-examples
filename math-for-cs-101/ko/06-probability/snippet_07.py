"""Generated from book-content article."""

def expected_value(values, probs):
    return sum(v * p for v, p in zip(values, probs, strict=False))


def variance(values, probs):
    mu = expected_value(values, probs)
    return sum(p * (v - mu) ** 2 for v, p in zip(values, probs, strict=False))
