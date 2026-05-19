"""Tests for ep01 in Software Engineering 101."""

from ko.ep01_metrics import compute_process_metrics


def test_ep01_metrics_from_fixture():
    """Test ep01 metrics from fixture."""
    m = compute_process_metrics("fixtures/ep01_events.json")
    assert m["lead_time_hours"] == 48.0
    assert m["cycle_time_hours"] == 24.0
