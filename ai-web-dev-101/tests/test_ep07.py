"""Tests for ep07 in Ai Web Dev 101."""

from conftest import load_module

module = load_module("ko/07-eval-improve/step01_eval_loop.py", "ep07")
keyword_score = module.keyword_score
evaluate_cases = module.evaluate_cases


def test_ep07_eval_metrics() -> None:
    """Test ep07 eval metrics."""
    assert keyword_score("월 9,900원 무료 체험", ["월 9,900원", "무료 체험"]) == 1.0
    summary = evaluate_cases(
        [
            {
                "response": "월 9,900원 무료 체험",
                "expected_keywords": ["월 9,900원", "무료 체험"],
            },
            {"response": "정보 없음", "expected_keywords": ["구독"]},
        ]
    )
    assert summary["avg_score"] == 0.5
