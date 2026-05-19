"""Tests for ep05 in Type Hints Python 101."""

from dataclasses import FrozenInstanceError

from ko.ep05_typeddict_dataclass import Point, profile_greeting


def test_ep05_typeddict_and_frozen_dataclass() -> None:
    """Test ep05 typeddict and frozen dataclass."""
    assert profile_greeting({"name": "kim"}) == "kim"
    p = Point(1, 2)
    try:
        p.x = 3  # type: ignore[misc]
        assert False, "FrozenInstanceError expected"
    except FrozenInstanceError:
        assert True
