def find_max(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError("empty list")
    current = numbers[0]
    for value in numbers[1:]:
        if value > current:
            current = value
    return current


if __name__ == "__main__":
    print(find_max([3, 7, 2, 9, 4]))
