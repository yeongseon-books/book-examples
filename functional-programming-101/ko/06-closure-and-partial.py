from __future__ import annotations

from functools import partial
from typing import Callable


def make_multiplier(factor: int) -> Callable[[int], int]:
    def _mul(value: int) -> int:
        return value * factor

    return _mul


def multiply(value: int, factor: int) -> int:
    return value * factor


def times_three() -> Callable[[int], int]:
    return partial(multiply, factor=3)


if __name__ == "__main__":
    print(make_multiplier(2)(10), times_three()(10))
