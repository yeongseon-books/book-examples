"""Algorithms Python 101 - Episode 1: Dp."""


def climb_stairs(n: int) -> int:
    """Climb stairs."""
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


if __name__ == "__main__":
    print(climb_stairs(7))
