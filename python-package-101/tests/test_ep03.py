"""Tests for ep03 in Python Package 101."""

from pathlib import Path

from common import ep03_parse_dependencies


def test_ep03_parse_pep508_dependencies() -> None:
    """Test ep03 parse pep508 dependencies."""
    out = ep03_parse_dependencies(Path("fixtures/sample_pyproject.toml"))
    assert len(out) >= 2
    assert out[0]["valid"] is True
    assert out[1]["marker"] is not None
