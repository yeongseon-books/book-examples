"""Tests for ep01 in Information Security 101."""

from common import risk_score


def test_risk_score():
    """Test risk score."""
    assert risk_score(3, 5) == 15
