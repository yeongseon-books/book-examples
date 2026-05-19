"""Tests for ep10 in Sqlalchemy 101."""

from ko import ep10_production_patterns


def test_ep10_production_patterns() -> None:
    """Test ep10 production patterns."""
    result = ep10_production_patterns.run()
    assert result["pool"] == "configured"
    assert result["retry"] in {"ok", "recovered"}
    assert result["scoped"] == "1"
    assert "Alembic" in result["migration"]
