"""Tests for ep01 in Technical Writing 101."""

from en.ep01_readability import analyze as en_analyze
from ko.ep01_readability import analyze as ko_analyze


def test_ep01_readability_scores():
    """Test ep01 readability scores."""
    en = en_analyze("fixtures/ep01_en.md")
    ko = ko_analyze("fixtures/ep01_ko.md")
    assert en["flesch_like"] > 0
    assert ko["char_per_sentence"] > 0
