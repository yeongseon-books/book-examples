from en.mymath import add, sub


def compute_pair(x: int, y: int) -> tuple[int, int]:
    return add(x, y), sub(x, y)


def main() -> None:
    plus, minus = compute_pair(7, 3)
    print("sum:", plus)
    print("difference:", minus)


if __name__ == "__main__":
    main()
