from dataclasses import dataclass


@dataclass(frozen=True)
class LineItem:
    price: int
    qty: int


def line_total(item: LineItem) -> int:
    return item.price * item.qty


def total(items: list[LineItem]) -> int:
    return sum(line_total(item) for item in items)


@dataclass(frozen=True)
class Range:
    lo: int
    hi: int


def in_range(value: int, r: Range) -> bool:
    return r.lo <= value <= r.hi
