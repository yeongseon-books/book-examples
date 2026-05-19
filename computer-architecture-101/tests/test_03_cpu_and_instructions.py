"""Tests for 03 cpu and instructions in Computer Architecture 101."""

from conftest import load_module

mod = load_module("ko/03-cpu-and-instructions.py", "ep03")


def test_tiny_isa_sample_program() -> None:
    """Test tiny isa sample program."""
    mem_result, reg_result = mod.run_sample_program()
    assert mem_result == 42
    assert reg_result == 42
