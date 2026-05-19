from itertools import combinations, permutations
from math import factorial


def npr(n, r):
    return factorial(n) // factorial(n - r)


def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def multinomial(counts):
    total = sum(counts)
    out = factorial(total)
    for c in counts:
        out //= factorial(c)
    return out


def derangements(n):
    s = 0
    for k in range(n + 1):
        s += ((-1) ** k) / factorial(k)
    return round(factorial(n) * s)


def stirling2(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + j * dp[i - 1][j]
    return dp[n][k]


def all_permutations(xs, r):
    return list(permutations(xs, r))


def all_combinations(xs, r):
    return list(combinations(xs, r))
