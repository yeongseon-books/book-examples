"""Tests for 10 operable devops flow in Devops 101."""

from ko import _10_operable_devops_flow as ep10


def test_end_to_end_happy_path_and_metrics_version() -> None:
    """Test end to end happy path and metrics version."""
    result = ep10.run_golden_path("v3.4.1")
    assert result["pipeline"] == "passed"
    assert result["deployment_healthy"] is True
    assert result["deployed_version"] == "v3.4.1"
    assert result["incident_opened"] is False
    assert result["metrics"]["error_rate_window_avg"] < 0.01
