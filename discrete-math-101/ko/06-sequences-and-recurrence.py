"""Discrete Math 101 - Episode 6: Sequences and recurrence."""

from functools import cache


def fib_naive(n):
    """Fib naive."""
    if n < 0:
        raise ValueError("n must be >= 0")
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)


@cache
def fib_memo(n):
    """Fib memo."""
    if n < 0:
        raise ValueError("n must be >= 0")
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)


def fib_matrix(n):
    """Fib matrix."""
    if n < 0:
        raise ValueError("n must be >= 0")

    def mul(a, b):
        """Mul."""
        return [
            [
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1],
            ],
            [
                a[1][0] * b[0][0] + a[1][1] * b[1][0],
                a[1][0] * b[0][1] + a[1][1] * b[1][1],
            ],
        ]

    def mpow(m, e):
        """Mpow."""
        r = [[1, 0], [0, 1]]
        while e:
            if e & 1:
                r = mul(r, m)
            m = mul(m, m)
            e >>= 1
        return r

    if n == 0:
        return 0
    return mpow([[1, 1], [1, 0]], n - 1)[0][0]


def recurrence_closed(n):
    """Recurrence closed."""
    if n < 0:
        raise ValueError("n must be >= 0")
    return 2**n - 1


def recurrence_iter(n):
    """Recurrence iter."""
    if n < 0:
        raise ValueError("n must be >= 0")
    t = 0
    for _ in range(n):
        t = 2 * t + 1
    return t
