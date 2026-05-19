"""Tests for ep04 in Python 101."""

from en.ep04_collections import update_contact_book


def test_contact_book_update() -> None:
    """Test contact book update."""
    book: dict[str, str] = {}
    update_contact_book(book, "Kim", "010")
    assert book["Kim"] == "010"
