"""Tests for ep03 in Operating Systems 101."""

from common import ep03_scheduler


def test_ep03_scheduler_orders():
    """Test ep03 scheduler orders."""
    out = ep03_scheduler(["A", "B", "C"], quantum=2)
    assert out["fifo"] == ["A", "B", "C"]
    assert out["round_robin"].count("A") == 2
    assert out["round_robin"][0] == "A"
