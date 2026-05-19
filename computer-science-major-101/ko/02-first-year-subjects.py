def set_operations(a: set[int], b: set[int]) -> dict[str, set[int]]:
    return {
        "union": a | b,
        "intersection": a & b,
        "difference": a - b,
    }


def mod_pow(base: int, exponent: int, mod: int) -> int:
    return pow(base, exponent, mod)


def verify_induction_sum(limit: int = 100) -> bool:
    for n in range(1, limit + 1):
        left = sum(range(1, n + 1))
        right = n * (n + 1) // 2
        if left != right:
            return False
    return True


if __name__ == "__main__":
    print(set_operations({1, 2, 3}, {3, 4, 5}))
    print(mod_pow(7, 5, 13))
    print(verify_induction_sum(100))
