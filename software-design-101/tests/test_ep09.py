"""Tests for ep09 in Software Design 101."""

from ko.ep09_solid_cupid import (
    composable_demo,
    dependency_inversion_demo,
    single_responsibility_demo,
)


def test_ep09_principles_examples() -> None:
    """Test ep09 principles examples."""
    assert "srp" in single_responsibility_demo()
    assert "dip" in dependency_inversion_demo()
    assert "composable" in composable_demo()
