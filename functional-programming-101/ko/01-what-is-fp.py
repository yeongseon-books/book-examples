"""Functional Programming 101 - Episode 1: What is fp."""

from __future__ import annotations

from common import pipe


def price_pipeline(price: int) -> int:
    """Price pipeline."""
    return pipe(lambda x: x * 2, lambda x: x - 300, lambda x: int(x * 0.9))(price)


if __name__ == "__main__":
    print(price_pipeline(5000))
