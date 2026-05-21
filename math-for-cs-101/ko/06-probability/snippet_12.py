"""Generated from book-content article."""

def expected(values, probs):
    return sum(v * p for v, p in zip(values, probs))

def variance(values, probs):
    mu = expected(values, probs)
    return sum(p * (v - mu) ** 2 for v, p in zip(values, probs))

vals = [0, 1, 2, 3]
probs = [0.1, 0.2, 0.5, 0.2]
print(expected(vals, probs), variance(vals, probs))
