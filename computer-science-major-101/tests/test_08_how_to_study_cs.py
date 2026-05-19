"""Tests for 08 how to study cs in Computer Science Major 101."""

from conftest import load_module


def test_sm2_increases_then_resets_interval() -> None:
    """Test sm2 increases then resets interval."""
    mod = load_module("ko/08-how-to-study-cs.py")
    state = mod.CardState(repetitions=0, interval=0, easiness=2.5)
    state = mod.sm2_step(state, 5)
    assert state.interval == 1
    state = mod.sm2_step(state, 5)
    assert state.interval == 6
    state = mod.sm2_step(state, 2)
    assert state.repetitions == 0
    assert state.interval == 1
