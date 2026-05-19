"""Tests for ep02 in Web Development 101."""

from pathlib import Path

from en.ep02_html_css_js import run


def test_ep02_html_structure_validator():
    """Test ep02 html structure validator."""
    fixture = Path(__file__).resolve().parent.parent / "fixtures" / "index.html"
    out = run(str(fixture))
    assert out["h1_count"] == 1
    assert out["has_charset"] is True
    assert out["has_viewport"] is True
