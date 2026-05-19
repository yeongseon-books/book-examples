import math


def ncr(n, r):
    return math.comb(n, r)


def npr(n, r):
    return math.perm(n, r)


def pigeonhole(items, holes):
    return items > holes
