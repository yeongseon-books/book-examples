def two_sum_bruteforce(nums: list[int], target: int) -> tuple[list[int], int]:
    ops = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            ops += 1
            if nums[i] + nums[j] == target:
                return [i, j], ops
    return [], ops


def two_sum_optimal(nums: list[int], target: int) -> tuple[list[int], int]:
    seen: dict[int, int] = {}
    ops = 0
    for i, n in enumerate(nums):
        ops += 1
        if target - n in seen:
            return [seen[target - n], i], ops
        seen[n] = i
    return [], ops
