"""Python 101 - Episode 4: Collections."""


def update_contact_book(book: dict[str, str], name: str, phone: str) -> dict[str, str]:
    """Update contact book."""
    book[name] = phone
    return book


def collection_snapshot() -> dict[str, object]:
    """Collection snapshot."""
    items = ["a", "b"]
    items.append("c")
    pair = (10, 20)
    tags = {"python", "basic"}
    mapping = {"lang": "python"}
    mapping["level"] = "beginner"
    return {"list": items, "tuple": pair, "set": tags, "dict": mapping}


def main() -> None:
    """Main."""
    print(collection_snapshot())
    book = {}
    update_contact_book(book, "Jisoo", "010-1111-2222")
    print(book)


if __name__ == "__main__":
    main()
