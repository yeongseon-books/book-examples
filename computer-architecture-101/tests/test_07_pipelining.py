from conftest import load_module


mod = load_module("ko/07-pipelining.py", "ep07")


def test_pipelined_cycles_better_than_non_pipelined() -> None:
    result = mod.sample_comparison()
    assert result["pipe_cycles"] < result["seq_cycles"]
    assert result["pipe_cpi"] < result["seq_cpi"]
