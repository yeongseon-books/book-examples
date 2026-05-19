"""Tests for ep07 in Software Engineering 101."""

from pathlib import Path

from ko.ep07_docs import docstring_coverage, readme_quality_score


def test_ep07_docs_quality():
    """Test ep07 docs quality."""
    code = Path("fixtures/ep07_sample.py").read_text(encoding="utf-8")
    readme = Path("fixtures/ep07_readme.md").read_text(encoding="utf-8")
    cov = docstring_coverage(code)
    assert cov["coverage"] == 0.5
    assert readme_quality_score(readme) == 4
