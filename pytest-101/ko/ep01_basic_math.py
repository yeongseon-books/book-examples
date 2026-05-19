def add(a: int, b: int) -> int:
    return a + b


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out
