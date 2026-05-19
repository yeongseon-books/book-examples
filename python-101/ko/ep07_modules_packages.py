"""Python 101 - Episode 7: Modules packages."""

from ko.mymath import add, sub


def compute_pair(x: int, y: int) -> tuple[int, int]:
    """Compute pair."""
    return add(x, y), sub(x, y)


def main() -> None:
    """Main."""
    plus, minus = compute_pair(7, 3)
    print("합:", plus)
    print("차:", minus)


if __name__ == "__main__":
    main()
