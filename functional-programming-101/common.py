"""Shared utilities and domain models for Functional Programming 101."""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass, replace
from functools import reduce
from itertools import count, islice
from operator import add
from typing import Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


@dataclass(frozen=True)
class CartItem:
    """Cart item."""

    name: str
    unit_price: int
    quantity: int


@dataclass(frozen=True)
class ImmutableState:
    """Immutable state."""

    values: tuple[int, ...]


@dataclass
class SideEffectCounter:
    """Side effect counter."""

    calls: int = 0

    def tick(self) -> None:
        """Tick."""
        self.calls += 1


@dataclass(frozen=True)
class LazyStream(Generic[T]):
    """Lazy stream."""

    source: Iterable[T]

    def map(self, fn: Callable[[T], U]) -> LazyStream[U]:
        """Map."""
        return LazyStream(fn(x) for x in self.source)

    def filter(self, pred: Callable[[T], bool]) -> LazyStream[T]:
        """Filter."""
        return LazyStream(x for x in self.source if pred(x))

    def take(self, n: int) -> list[T]:
        """Take."""
        return list(islice(self.source, n))


def compose(*funcs: Callable[[object], object]) -> Callable[[object], object]:
    """Compose."""

    def _apply(value: object) -> object:
        """Apply."""
        result = value
        for fn in reversed(funcs):
            result = fn(result)
        return result

    return _apply


def pipe(*funcs: Callable[[object], object]) -> Callable[[object], object]:
    """Pipe."""

    def _apply(value: object) -> object:
        """Apply."""
        result = value
        for fn in funcs:
            result = fn(result)
        return result

    return _apply


def immutable_append(state: ImmutableState, value: int) -> ImmutableState:
    """Immutable append."""
    return replace(state, values=(*state.values, value))


def impossible_mutation(state: ImmutableState) -> type[Exception] | None:
    """Impossible mutation."""
    try:
        state.values = *state.values, 999
    except Exception as exc:
        return type(exc)
    return None


def naturals(start: int = 0) -> Iterator[int]:
    """Naturals."""
    yield from count(start)


def reduce_sum(values: Iterable[int]) -> int:
    """Reduce sum."""
    return reduce(add, values, 0)
