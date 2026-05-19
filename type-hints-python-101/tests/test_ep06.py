"""Tests for ep06 in Type Hints Python 101."""

from ko.ep06_protocol_structural import pick_smallest


def test_ep06_protocol_structural_typing() -> None:
    """Test ep06 protocol structural typing."""
    assert pick_smallest([3, 1, 2]) == 1
