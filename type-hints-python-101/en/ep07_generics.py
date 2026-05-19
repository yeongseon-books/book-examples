"""Type Hints Python 101 - Episode 7: Generics."""

from collections.abc import Callable
from typing import Generic, ParamSpec, TypeVar

T = TypeVar("T")
N = TypeVar("N", bound=int)
P = ParamSpec("P")
R = TypeVar("R")


class Stack(Generic[T]):
    """Stack."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Push."""
        self._items.append(item)

    def pop(self) -> T:
        """Pop."""
        if not self._items:
            raise IndexError("empty stack")
        return self._items.pop()


def clamp_to_zero(value: N) -> N:
    """Clamp to zero."""
    return value if value > 0 else type(value)(0)


def call_with_log(
    func: Callable[P, R], *args: P.args, **kwargs: P.kwargs
) -> tuple[str, R]:
    """Call with log."""
    result = func(*args, **kwargs)
    return ("called", result)
