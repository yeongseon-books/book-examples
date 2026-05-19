from __future__ import annotations

from dataclasses import dataclass, replace
from functools import reduce
from itertools import count, islice
from operator import add
from typing import Callable, Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


@dataclass(frozen=True)
class CartItem:
    name: str
    unit_price: int
    quantity: int


@dataclass(frozen=True)
class ImmutableState:
    values: tuple[int, ...]


@dataclass
class SideEffectCounter:
    calls: int = 0

    def tick(self) -> None:
        self.calls += 1


@dataclass(frozen=True)
class LazyStream(Generic[T]):
    source: Iterable[T]

    def map(self, fn: Callable[[T], U]) -> LazyStream[U]:
        return LazyStream(fn(x) for x in self.source)

    def filter(self, pred: Callable[[T], bool]) -> LazyStream[T]:
        return LazyStream(x for x in self.source if pred(x))

    def take(self, n: int) -> list[T]:
        return list(islice(self.source, n))


def compose(*funcs: Callable[[object], object]) -> Callable[[object], object]:
    def _apply(value: object) -> object:
        result = value
        for fn in reversed(funcs):
            result = fn(result)
        return result

    return _apply


def pipe(*funcs: Callable[[object], object]) -> Callable[[object], object]:
    def _apply(value: object) -> object:
        result = value
        for fn in funcs:
            result = fn(result)
        return result

    return _apply


def immutable_append(state: ImmutableState, value: int) -> ImmutableState:
    return replace(state, values=(*state.values, value))


def impossible_mutation(state: ImmutableState) -> type[Exception] | None:
    try:
        setattr(state, "values", (*state.values, 999))
    except Exception as exc:
        return type(exc)
    return None


def naturals(start: int = 0) -> Iterator[int]:
    yield from count(start)


def reduce_sum(values: Iterable[int]) -> int:
    return reduce(add, values, 0)
