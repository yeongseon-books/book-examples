"""Clean Code 101 - Episode 1: Small functions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class LineItem:
    """Line item."""

    price: int
    qty: int


def line_total(item: LineItem) -> int:
    """Line total."""
    return item.price * item.qty


def total(items: list[LineItem]) -> int:
    """Total."""
    return sum(line_total(item) for item in items)


@dataclass(frozen=True)
class Range:
    """Range."""

    lo: int
    hi: int


def in_range(value: int, r: Range) -> bool:
    """In range."""
    return r.lo <= value <= r.hi
