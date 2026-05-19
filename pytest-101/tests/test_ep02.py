"""Tests for ep02 in Pytest 101."""

from en.ep02_parser import parse_key_value


def test_ep02_parse_key_value_basic_assertion():
    """Test ep02 parse key value basic assertion."""
    parsed = parse_key_value("name=pytest, level=101")
    assert parsed == {"name": "pytest", "level": "101"}


def test_ep02_parse_key_value_invalid_input_raises():
    """Test ep02 parse key value invalid input raises."""
    import pytest

    with pytest.raises(ValueError):
        parse_key_value("missing-separator")
