def combine_values(
    a: int, b: int = 0, *args: int, scale: int = 1, **kwargs: int
) -> int:
    base = a + b + sum(args)
    bonus = sum(kwargs.values())
    return (base + bonus) * scale


def main() -> None:
    print(combine_values(1, 2))
    print(combine_values(1, 2, 3, 4, scale=2, extra=5))


if __name__ == "__main__":
    main()
