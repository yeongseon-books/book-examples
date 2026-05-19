"""Tests for ep04 in Sqlalchemy 101."""

from ko import ep04_orm_declarative


def test_ep04_orm_declarative() -> None:
    """Test ep04 orm declarative."""
    assert ep04_orm_declarative.run() == "articles"
