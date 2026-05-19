from functools import cache


def fib_naive(n):
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)


@cache
def fib_memo(n):
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)


def fib_matrix(n):
    def mul(a, b):
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
    return 2**n - 1


def recurrence_iter(n):
    t = 0
    for _ in range(n):
        t = 2 * t + 1
    return t
