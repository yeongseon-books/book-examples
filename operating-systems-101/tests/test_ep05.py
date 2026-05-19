"""Tests for ep05 in Operating Systems 101."""

from common import ep05_producer_consumer


def test_ep05_producer_consumer_balanced():
    """Test ep05 producer consumer balanced."""
    out = ep05_producer_consumer(count=8, capacity=2)
    assert out["produced"] == list(range(8))
    assert sorted(out["consumed"]) == list(range(8))
