"""Tests for ep03 in Software Engineering 101."""

from pathlib import Path

from ko.ep03_design_impl import design_doc_completeness, generate_impl_skeleton


def test_ep03_design_and_skeleton():
    """Test ep03 design and skeleton."""
    text = Path("fixtures/ep03_design_doc.md").read_text(encoding="utf-8")
    r = design_doc_completeness(text)
    assert r["score"] == 1.0
    assert "implement_auth" in generate_impl_skeleton("auth")
