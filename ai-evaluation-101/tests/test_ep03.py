"""Tests for ep03 in Ai Evaluation 101."""

from conftest import load_module


def test_ep03_metrics_reward_paraphrase_partially() -> None:
    """Test ep03 metrics reward paraphrase partially."""
    module = load_module(
        "ko/03-deterministic-metrics/step01_deterministic_metrics.py", "ep03"
    )
    result = module.run()
    assert result["em_good"] == 1.0
    assert result["em_para"] == 0.0
    assert result["bleu_para"] > 0.3
