"""Tests for ep08 in Technical Writing 101."""

from en.ep08_tutorial_validator import analyze


def test_ep08_tutorial_structure():
    """Test ep08 tutorial structure."""
    good = analyze("fixtures/ep08_tutorial_good.md")
    bad = analyze("fixtures/ep08_tutorial_bad.md")
    assert (
        good["has_prerequisites"]
        and good["has_expected_outcome"]
        and good["step_count"] >= 2
    )
    assert not bad["has_prerequisites"] or bad["step_count"] == 0
