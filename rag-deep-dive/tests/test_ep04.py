"""Tests for ep04 in Rag Deep Dive."""

from ko.ep04_prompt_builder import build_prompt


def test_ep04_prompt_has_citation_tags_and_budget():
    """Test ep04 prompt has citation tags and budget."""
    contexts = ["x" * 50, "y" * 50, "z" * 50]
    prompt = build_prompt("What is RAG?", contexts, budget_chars=90)
    assert "[C1]" in prompt
    assert "Answer:" in prompt
