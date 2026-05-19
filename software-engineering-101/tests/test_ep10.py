"""Tests for ep10 in Software Engineering 101."""

from pathlib import Path

from en.ep10_quality import combined_quality_report


def test_ep10_quality_report():
    """Test ep10 quality report."""
    code = Path("fixtures/ep10_code.py").read_text(encoding="utf-8")
    report = combined_quality_report(code)
    assert report["testability"] == 0.5
    assert report["readability"] > 0
    assert 0 <= report["maintainability"] <= 1
