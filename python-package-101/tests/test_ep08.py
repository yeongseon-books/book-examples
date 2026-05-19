"""Tests for ep08 in Python Package 101."""

from pathlib import Path

from common import ep08_count_annotations


def test_ep08_type_hint_check() -> None:
    """Test ep08 type hint check."""
    out = ep08_count_annotations(Path("fixtures/sample_module.py"))
    assert out["ok"] is True
