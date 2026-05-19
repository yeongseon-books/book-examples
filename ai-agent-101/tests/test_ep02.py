"""Tests for ep02 in Ai Agent 101."""

from conftest import load_module

build_context = load_module(
    "ko/02-context-engineering/step01_context_builder.py", "ep02"
).build_context


def test_ep02_context_contains_priority_sections() -> None:
    """Test ep02 context contains priority sections."""
    context = build_context("S", {"task": "t"}, ["doc"], ["h1", "h2"], "q")
    assert "# System" in context
    assert "# Query" in context
