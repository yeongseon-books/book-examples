"""Tests for 09 parallelism and multicore in Computer Architecture 101."""

from conftest import load_module

mod = load_module("ko/09-parallelism-and-multicore.py", "ep09")


def test_threaded_vector_add_matches_sequential() -> None:
    """Test threaded vector add matches sequential."""
    a = list(range(1000))
    b = list(range(2000, 3000))
    assert mod.vector_add_threaded(a, b, workers=4) == mod.vector_add_sequential(a, b)
