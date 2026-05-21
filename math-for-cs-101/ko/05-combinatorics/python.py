"""Generated from book-content article."""

import math


def npr(n, r):
    return math.factorial(n) // math.factorial(n-r)

def ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

print(npr(10, 3), ncr(10, 3))
