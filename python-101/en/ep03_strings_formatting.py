"""Python 101 - Episode 3: Strings formatting."""


def normalize_words(text: str) -> list[str]:
    """Normalize words."""
    pieces = [part.strip().lower() for part in text.split(",")]
    return [p for p in pieces if p]


def main() -> None:
    """Main."""
    name = "Python"
    version = 3.12
    print(f"f-string: {name} {version}")
    print(f"format: {name} {version:.1f}")
    print(f"percent: {name} {version:.1f}")
    words = normalize_words(" apple, Banana , , cherry ")
    print("|".join(words))


if __name__ == "__main__":
    main()
