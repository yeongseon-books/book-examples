"""Tests for ep10 in Pytest 101."""

from en.ep10_refactor_demo import GLOBAL_QUEUE, enqueue_global, enqueue_with_dependency


def test_ep10_before_refactor_global_state_side_effect():
    """Test ep10 before refactor global state side effect."""
    GLOBAL_QUEUE.clear()
    enqueue_global("x")
    assert GLOBAL_QUEUE == ["x"]


def test_ep10_after_refactor_injected_dependency_isolated():
    """Test ep10 after refactor injected dependency isolated."""
    sink: list[str] = []
    enqueue_with_dependency("x", sink)
    assert sink == ["x"]
