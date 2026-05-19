"""Python 101 - Episode 8: File io exceptions."""

from pathlib import Path


def parse_csv_like(text: str) -> list[tuple[str, int]]:
    """Parse csv like."""
    rows: list[tuple[str, int]] = []
    for line in text.strip().splitlines():
        name, score = line.split(",")
        rows.append((name.strip(), int(score.strip())))
    return rows


def write_and_read_demo(path: Path, text: str) -> str:
    """Write and read demo."""
    try:
        with path.open("w", encoding="utf-8") as file:
            file.write(text)
        with path.open("r", encoding="utf-8") as file:
            return file.read()
    except OSError:
        return ""
    finally:
        pass


def main() -> None:
    """Main."""
    sample = "Alice,90\nBob,85"
    print(parse_csv_like(sample))


if __name__ == "__main__":
    main()
