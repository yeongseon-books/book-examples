"""Tests for 07 pipelining in Computer Architecture 101."""

from conftest import load_module

mod = load_module("ko/07-pipelining.py", "ep07")


def test_pipelined_cycles_better_than_non_pipelined() -> None:
    """Test pipelined cycles better than non pipelined."""
    result = mod.sample_comparison()
    assert result["pipe_cycles"] < result["seq_cycles"]
    assert result["pipe_cpi"] < result["seq_cpi"]
