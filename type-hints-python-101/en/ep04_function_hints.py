"""Type Hints Python 101 - Episode 4: Function hints."""

from collections.abc import Callable
from typing import TypeAlias

IntOp: TypeAlias = Callable[[int, int], int]


def run_op(op: IntOp, left: int = 1, right: int = 2) -> int:
    """Run op."""
    return op(left, right)


def sum_all(*args: int, scale: int = 1, **kwargs: int) -> int:
    """Sum all."""
    return (sum(args) + sum(kwargs.values())) * scale
