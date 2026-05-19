"""Tests for ep02 in Python Package 101."""

from pathlib import Path

from common import ep02_validate_project_structure


def test_ep02_validate_src_layout(tmp_path: Path) -> None:
    """Test ep02 validate src layout."""
    (tmp_path / "src" / "sample").mkdir(parents=True)
    out = ep02_validate_project_structure(tmp_path)
    assert out["status"] == "src-layout"
