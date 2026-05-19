"""Algorithms 101 - Episode 1: Knapsack dp."""

from __future__ import annotations


def knapsack(weights: list[int], values: list[int], cap: int) -> int:
    """Knapsack."""
    n = len(weights)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w, v = weights[i - 1], values[i - 1]
        for c in range(cap + 1):
            dp[i][c] = dp[i - 1][c]
            if w <= c:
                dp[i][c] = max(dp[i][c], dp[i - 1][c - w] + v)
    return dp[n][cap]


def run() -> dict[str, object]:
    """Run."""
    w = [2, 3, 4, 5]
    v = [3, 4, 5, 6]
    c = 5
    return {"weights": w, "values": v, "cap": c, "best": knapsack(w, v, c)}


if __name__ == "__main__":
    print(run())
