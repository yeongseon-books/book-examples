"""Tests for ep09 in Ai Evaluation 101."""

from conftest import load_module


def test_ep09_welch_detects_variant_a_advantage() -> None:
    """Test ep09 welch detects variant a advantage."""
    module = load_module("ko/09-ab-testing-llms/step01_ab_welch.py", "ep09")
    result = module.run()
    assert result["is_better"] is True
    assert result["p_value"] < 0.05
