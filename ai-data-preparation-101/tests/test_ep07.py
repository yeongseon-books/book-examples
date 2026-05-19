"""Tests for ep07 in Ai Data Preparation 101."""

from conftest import run_dict


def test_ep07_synthetic() -> None:
    """Test ep07 synthetic."""
    result = run_dict("ko/07-synthetic-data-generation/step01_self_instruct_mock.py")
    assert result["count"] == 2
    assert "samples" in result
