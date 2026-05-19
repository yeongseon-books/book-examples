"""Data Structures Python 101 - Episode 7: Heaps and priority queues."""

import heapq


def min_heap_pop_order(values: list[int]) -> list[int]:
    """Min heap pop order."""
    heap = values[:]
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]


def top_n_largest(values: list[int], n: int) -> list[int]:
    """Top n largest."""
    return heapq.nlargest(n, values)


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    """Merge sorted lists."""
    return list(heapq.merge(*lists))


if __name__ == "__main__":
    print(min_heap_pop_order([5, 1, 4, 3, 2]))
    print(top_n_largest([5, 1, 9, 3, 7], 3))
    print(merge_sorted_lists([[1, 4, 7], [2, 3, 8], [0, 5, 9]]))
