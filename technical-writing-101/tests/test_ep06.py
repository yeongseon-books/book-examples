"""Tests for ep06 in Technical Writing 101."""

from en.ep06_figure_table_linter import analyze


def test_ep06_figure_table_rules():
    """Test ep06 figure table rules."""
    good = analyze("fixtures/ep06_good.md")
    bad = analyze("fixtures/ep06_bad.md")
    assert good["images_missing_alt"] == 0 and good["table_caption_ok"]
    assert bad["images_missing_alt"] > 0 or not bad["table_caption_ok"]
