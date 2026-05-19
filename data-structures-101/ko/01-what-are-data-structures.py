"""Data Structures 101 - Episode 1: What are data structures."""

from __future__ import annotations


class OperationCounter:
    """Operation counter."""

    def __init__(self) -> None:
        self.c = 0

    def inc(self, _name: str, amount: int = 1) -> None:
        """Inc."""
        self.c += amount

    def total(self) -> int:
        """Total."""
        return self.c


def find_duplicates_quadratic(values: list[int]) -> tuple[list[int], int]:
    """Find duplicates quadratic."""
    counter = OperationCounter()
    out: list[int] = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            counter.inc("cmp")
            if values[i] == values[j] and values[i] not in out:
                out.append(values[i])
    return out, counter.total()


def find_duplicates_sorted(values: list[int]) -> tuple[list[int], int]:
    """Find duplicates sorted."""
    counter = OperationCounter()
    arr = values[:]
    arr.sort()
    out: list[int] = []
    for i in range(1, len(arr)):
        counter.inc("cmp")
        if arr[i] == arr[i - 1] and (not out or out[-1] != arr[i]):
            out.append(arr[i])
    return out, counter.total()


class TinyHashSet:
    """Tiny hash set."""

    def __init__(self, capacity: int = 16) -> None:
        self._buckets: list[list[int]] = [[] for _ in range(capacity)]

    def _index(self, value: int) -> int:
        """Index."""
        return value % len(self._buckets)

    def add(self, value: int) -> bool:
        """Add."""
        bucket = self._buckets[self._index(value)]
        for item in bucket:
            if item == value:
                return False
        bucket.append(value)
        return True


def find_duplicates_hash(values: list[int]) -> tuple[list[int], int]:
    """Find duplicates hash."""
    counter = OperationCounter()
    seen = TinyHashSet()
    dup = TinyHashSet()
    out: list[int] = []
    for value in values:
        counter.inc("read")
        if not seen.add(value) and dup.add(value):
            out.append(value)
    return out, counter.total()


def run_demo(values: list[int]) -> dict[str, tuple[list[int], int]]:
    """Run demo."""
    return {
        "quadratic": find_duplicates_quadratic(values),
        "sorted": find_duplicates_sorted(values),
        "hash": find_duplicates_hash(values),
    }


if __name__ == "__main__":
    sample = [1, 3, 2, 3, 5, 1, 8, 9, 8]
    print(run_demo(sample))
