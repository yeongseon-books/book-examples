"""Tests for ep01 in Python 101."""

from en.ep01_hello_world import get_runtime_info


def test_runtime_info_keys() -> None:
    """Test runtime info keys."""
    info = get_runtime_info()
    assert "python_version" in info
    assert "platform" in info
