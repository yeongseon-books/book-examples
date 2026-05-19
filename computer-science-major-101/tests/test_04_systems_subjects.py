"""Tests for 04 systems subjects in Computer Science Major 101."""

from conftest import load_module


def test_round_robin_uses_all_cpu_bursts() -> None:
    """Test round robin uses all cpu bursts."""
    mod = load_module("ko/04-systems-subjects.py")
    processes = [mod.PCB(1, 5, 5), mod.PCB(2, 3, 3)]
    timeline = mod.round_robin(processes, quantum=2)
    consumed = {1: 0, 2: 0}
    for pid, spent in timeline:
        consumed[pid] += spent
    assert consumed == {1: 5, 2: 3}
