"""Tests for 01 what is computer architecture in Computer Architecture 101."""

from conftest import load_module

mod = load_module("ko/01-what-is-computer-architecture.py", "ep01")


def test_von_neumann_loop_stores_result() -> None:
    """Test von neumann loop stores result."""
    assert mod.run_program() == 12
