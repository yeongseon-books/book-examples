"""Generated from book-content article."""

import math


def master_case(a, b, k):
    alpha = math.log(a, b)
    if k < alpha:
        return "case1: Theta(n^{log_b a})"
    if abs(k - alpha) < 1e-12:
        return "case2: Theta(n^k log n)"
    return "case3: Theta(n^k) (regularity check needed)"

print(master_case(2, 2, 1))
print(master_case(3, 2, 1))
