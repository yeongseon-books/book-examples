from typing import Callable, TypeAlias

IntOp: TypeAlias = Callable[[int, int], int]


def run_op(op: IntOp, left: int = 1, right: int = 2) -> int:
    return op(left, right)


def sum_all(*args: int, scale: int = 1, **kwargs: int) -> int:
    return (sum(args) + sum(kwargs.values())) * scale
