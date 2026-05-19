"""Probability 101 - Episode 1: Monte carlo."""

from __future__ import annotations

from common import make_rng


def run(n: int = 100_000) -> dict[str, float]:
    """Run."""
    rng = make_rng()
    coins = rng.integers(0, 2, size=n)
    dice = rng.integers(1, 7, size=n)
    return {
        "p_head": float((coins == 1).mean()),
        "p_dice_even": float((dice % 2 == 0).mean()),
    }


if __name__ == "__main__":
    print(run())
