"""Tests for ep05 in Sre 101."""

from en.ep05_monitoring_windows import aggregate_window


def test_ep05_aggregator_percentiles():
    """Test ep05 aggregator percentiles."""
    out = aggregate_window([10, 20, 30, 40, 50], 10)
    assert out["count"] == 5
    assert out["rate"] == 0.5
    assert out["p50"] == 30
