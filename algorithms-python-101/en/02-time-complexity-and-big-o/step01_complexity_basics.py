"""Algorithms Python 101 - Episode 1: Complexity basics."""


def linear_search(data: list[int], target: int) -> int:
    """Linear search."""
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


def binary_search(sorted_data: list[int], target: int) -> int:
    """Binary search."""
    if not sorted_data:
        return -1
    left, right = 0, len(sorted_data) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_data[mid] == target:
            return mid
        if sorted_data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    print(linear_search([1, 2, 3, 4], 3), binary_search([1, 2, 3, 4], 3))
