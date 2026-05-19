import bisect


def bisect_search(sorted_data: list[int], target: int) -> int:
    pos = bisect.bisect_left(sorted_data, target)
    if pos < len(sorted_data) and sorted_data[pos] == target:
        return pos
    return -1


if __name__ == "__main__":
    print(bisect_search([1, 3, 5, 7, 9], 7))
