from typing import Protocol, runtime_checkable


@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, other: object) -> bool: ...


def pick_smallest(items: list[Comparable]) -> Comparable:
    if not items:
        raise ValueError("items must not be empty")
    smallest = items[0]
    for item in items[1:]:
        if item < smallest:
            smallest = item
    return smallest
