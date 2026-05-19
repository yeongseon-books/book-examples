"""Tests for ep03 in Sre 101."""

from en.ep03_sli_slo_sla import compute_sli, is_sla_breached, is_slo_met


def test_ep03_sli_slo_sla():
    """Test ep03 sli slo sla."""
    sli = compute_sli(995, 1000)
    assert is_slo_met(sli, 0.99)
    assert not is_sla_breached(sli, 0.95)
