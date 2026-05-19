"""Tests for ep08 in Portfolio Project 101."""

from pathlib import Path

from common import read_json
from ko.ep08_outline_generator import generate_blog_outline


def test_ep08_outline_generator() -> None:
    """Test ep08 outline generator."""
    outline = generate_blog_outline(read_json(Path("fixtures/project_metadata.json")))
    assert "## Problem" in outline
    assert "## Approach" in outline
    assert "## Result" in outline
