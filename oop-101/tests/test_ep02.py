"""Tests for ep02 in Oop 101."""

from ko.ep02_classes_and_instances import build_sample_books


def test_ep02_books_summary() -> None:
    """Test ep02 books summary."""
    books = build_sample_books()
    assert len(books) == 2
    assert books[0].summary().startswith("Fluent Python")
