from ko.mymath import add, sub


def compute_pair(x: int, y: int) -> tuple[int, int]:
    return add(x, y), sub(x, y)


def main() -> None:
    plus, minus = compute_pair(7, 3)
    print("합:", plus)
    print("차:", minus)


if __name__ == "__main__":
    main()
