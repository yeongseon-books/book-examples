"""Tests for ep03 in Type Hints Python 101."""

from ko.ep03_optional_union_literal_final import parse_maybe_int, traffic_action


def test_ep03_optional_union_literal_final() -> None:
    """Test ep03 optional union literal final."""
    assert parse_maybe_int("12") == 12
    assert parse_maybe_int("x") is None
    assert traffic_action("green") == "go"
