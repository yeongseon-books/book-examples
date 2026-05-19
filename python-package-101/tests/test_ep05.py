"""Tests for ep05 in Python Package 101."""

from pathlib import Path

from common import ep05_validate_metadata


def test_ep05_metadata_required_fields() -> None:
    """Test ep05 metadata required fields."""
    out = ep05_validate_metadata(Path("fixtures/sample_pyproject.toml"))
    assert out["valid"] is True
    assert out["docs_only_url"].startswith("https://test.pypi.org")
