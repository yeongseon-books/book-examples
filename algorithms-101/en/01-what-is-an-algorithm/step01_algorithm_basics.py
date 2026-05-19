from __future__ import annotations


def two_sum_hash(nums: list[int], target: int) -> tuple[int, int] | None:
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        comp = target - x
        if comp in seen:
            return (seen[comp], i)
        seen[x] = i
    return None


def run() -> dict[str, object]:
    data = [2, 7, 11, 15]
    pair = two_sum_hash(data, 9)
    return {"input": data, "target": 9, "pair": pair}


if __name__ == "__main__":
    print(run())
