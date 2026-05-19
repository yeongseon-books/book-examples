"""에피소드 04: 탐색 알고리즘 비교"""


def linear_search_count(arr: list[int], target: int) -> int:
    comparisons = 0
    for item in arr:
        comparisons += 1
        if item == target:
            return comparisons
    return comparisons


def binary_search_count(arr: list[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    comparisons = 0
    while lo <= hi:
        comparisons += 1
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return comparisons
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return comparisons


def comparison_table(sizes: list[int]) -> list[tuple[int, int, int]]:
    rows: list[tuple[int, int, int]] = []
    for n in sizes:
        arr = list(range(n))
        target = n - 1
        rows.append(
            (n, linear_search_count(arr, target), binary_search_count(arr, target))
        )
    return rows


if __name__ == "__main__":
    for row in comparison_table([10, 100, 1_000, 10_000]):
        print(f"n={row[0]:>5} linear={row[1]:>5} binary={row[2]:>3}")
