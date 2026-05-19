"""Data Structures 101 - Episode 8: Heaps."""

from __future__ import annotations


class MinHeap:
    """Min heap."""

    def __init__(self) -> None:
        self.data: list[int] = []

    def __len__(self) -> int:
        """Len."""
        return len(self.data)

    def peek(self) -> int:
        """Peek."""
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    def push(self, value: int) -> None:
        """Push."""
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def pop(self) -> int:
        """Pop."""
        if not self.data:
            raise IndexError("pop from empty heap")
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return top

    def _sift_up(self, idx: int) -> None:
        """Sift up."""
        while idx > 0:
            parent = (idx - 1) // 2
            if self.data[idx] < self.data[parent]:
                self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx: int) -> None:
        """Sift down."""
        n = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == idx:
                return
            self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
            idx = smallest


def heapsort(values: list[int]) -> list[int]:
    """Heapsort."""
    heap = MinHeap()
    for v in values:
        heap.push(v)
    return [heap.pop() for _ in range(len(heap))]
