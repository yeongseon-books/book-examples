"""Tests for ep06 in Ai Evaluation 101."""

from conftest import load_module


def test_ep06_rag_retrieval_scores_are_high_at_k2() -> None:
    """Test ep06 rag retrieval scores are high at k2."""
    module = load_module("ko/06-rag-evaluation/step01_rag_metrics.py", "ep06")
    result = module.run()
    assert result["precision_at_2"] == 1.0
    assert result["recall_at_2"] == 1.0
