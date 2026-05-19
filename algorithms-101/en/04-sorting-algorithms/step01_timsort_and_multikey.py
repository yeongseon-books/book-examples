from __future__ import annotations

from common import is_sorted_non_decreasing


def sort_numbers(values: list[int]) -> list[int]:
    return sorted(values)


def stable_multi_key(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    out = list(people)
    out.sort(key=lambda p: p[0])
    out.sort(key=lambda p: p[1])
    return out


def run() -> dict[str, object]:
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    people = [("Alice", 30), ("Bob", 25), ("Carol", 30), ("Dan", 25)]
    sorted_nums = sort_numbers(nums)
    return {
        "sorted_ok": is_sorted_non_decreasing(sorted_nums),
        "sorted_nums": sorted_nums,
        "people": stable_multi_key(people),
    }


if __name__ == "__main__":
    print(run())
