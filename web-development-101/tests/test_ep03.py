"""Tests for ep03 in Web Development 101."""

from pathlib import Path

from en.ep03_browser_dom import DOMBuilder, query_by_class, query_by_tag


def test_ep03_dom_builder_and_selectors():
    """Test ep03 dom builder and selectors."""
    html = (
        Path(__file__).resolve().parent.parent / "fixtures" / "index.html"
    ).read_text(encoding="utf-8")
    parser = DOMBuilder()
    parser.feed(html)
    assert len(query_by_tag(parser.root, "h1")) == 1
    assert len(query_by_class(parser.root, "card")) == 1
