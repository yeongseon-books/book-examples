def normalize_words(text: str) -> list[str]:
    pieces = [part.strip().lower() for part in text.split(",")]
    return [p for p in pieces if p]


def main() -> None:
    name = "Python"
    version = 3.12
    print(f"f-string: {name} {version}")
    print("format: {} {:.1f}".format(name, version))
    print("percent: %s %.1f" % (name, version))
    words = normalize_words(" apple, Banana , , cherry ")
    print("|".join(words))


if __name__ == "__main__":
    main()
