"""Tests for 06 cache and locality in Computer Architecture 101."""

from conftest import load_module

mod = load_module("ko/06-cache-and-locality.py", "ep06")


def test_sequential_has_higher_hit_rate_than_random() -> None:
    """Test sequential has higher hit rate than random."""
    seq_rate, rand_rate = mod.compare_locality(seed=7)
    assert seq_rate > rand_rate
