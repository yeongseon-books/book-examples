from en.ep04_collections import update_contact_book


def test_contact_book_update() -> None:
    book: dict[str, str] = {}
    update_contact_book(book, "Kim", "010")
    assert book["Kim"] == "010"
