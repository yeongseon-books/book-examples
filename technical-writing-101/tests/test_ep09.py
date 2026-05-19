"""Tests for ep09 in Technical Writing 101."""

from en.ep09_blog_docs_classifier import analyze


def test_ep09_classifier():
    """Test ep09 classifier."""
    blog = analyze("fixtures/ep09_blog.md")
    docs = analyze("fixtures/ep09_docs.md")
    assert blog["classification"] == "blog"
    assert docs["classification"] == "docs"
