"""Tests for ep10 in Python Dbapi 101."""

from en import ep10_production_patterns as ep


def test_ep10_retry_transaction_bulk_insert():
    """Test ep10 retry transaction bulk insert."""
    result = ep.run_demo()
    assert result["count"] == 3
