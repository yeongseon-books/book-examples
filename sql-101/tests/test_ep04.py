"""Tests for ep04 in Sql 101."""

from en.ep04_join import run_demo


def test_ep04_join_types():
    """Test ep04 join types."""
    out = run_demo()
    assert out["inner_count"] == 5
    assert out["left_nulls"] == 1
    assert out["right_emulated"] == 5
    assert out["cross_sample"] == 5
    assert out["self_pairs"] == 5
