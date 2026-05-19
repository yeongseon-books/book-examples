"""Tests for ep07 in Software Design 101."""

from ko.ep07_data_flow import run_pipeline


def test_ep07_pipeline() -> None:
    """Test ep07 pipeline."""
    assert run_pipeline("lang=python") == "LANG:PYTHON"
