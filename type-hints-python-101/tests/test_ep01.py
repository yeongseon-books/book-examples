"""Tests for ep01 in Type Hints Python 101."""

from ko.ep01_type_hint_overview import add


def test_ep01_add_and_runtime_check() -> None:
    """Test ep01 add and runtime check."""
    assert add(1, 2) == 3
    try:
        add("1", 2)  # type: ignore[arg-type]
        assert False, "TypeError expected"
    except TypeError:
        assert True
