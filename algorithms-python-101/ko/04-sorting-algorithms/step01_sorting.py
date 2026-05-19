"""Algorithms Python 101 - Episode 1: Sorting."""


def merge_sort(data: list[int]) -> list[int]:
    """Merge sort."""
    if len(data) <= 1:
        return data[:]
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    merged: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
