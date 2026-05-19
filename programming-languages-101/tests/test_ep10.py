"""Tests for ep10 in Programming Languages 101."""

from ko.ep10_design_checklist import score_language


def test_ep10_design_checklist():
    """Test ep10 design checklist."""
    out = score_language(7, 6, 7, 6)
    assert out["total"] == 26
    assert out["pass"] is True
