"""Tests for ep01 in Ai Data Preparation 101."""

from conftest import run_dict


def test_ep01_quality_report() -> None:
    """Test ep01 quality report."""
    result = run_dict("ko/01-why-data-preparation-matters/step01_quality_report.py")
    assert result["total"] == 5.0
    assert 0 < float(result["unique_ratio"]) <= 1
