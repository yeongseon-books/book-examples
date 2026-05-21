"""Generated from book-content article."""

def sum_formula(n: int) -> int:
    return n * (n + 1) // 2

def verify_sum(limit: int = 500):
    # base
    assert sum_formula(1) == 1
    # induction-like exhaustive check for small n
    for n in range(1, limit):
        left = sum_formula(n + 1)
        right = sum_formula(n) + (n + 1)
        assert left == right

verify_sum()
print("verified")
