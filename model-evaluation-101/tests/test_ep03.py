"""Tests for ep03 in Model Evaluation 101."""

from conftest import load_module

run = load_module("ko/03-limits-of-accuracy/step01_accuracy_trap.py", "ep03").run


def test_ep03_accuracy_trap_and_balanced_fix() -> None:
    """Test ep03 accuracy trap and balanced fix."""
    out = run()
    assert out["dummy_accuracy"] >= 0.9
    assert out["dummy_recall"] == 0.0
    assert out["balanced_recall"] > out["dummy_recall"]
