"""Tests for ep05 in Multimodal Ai 101."""

from conftest import load_module

run = load_module("ko/05-multimodal-rag/step01_multimodal_rag.py", "ep05").run


def test_ep05_rag_retrieves_fixture() -> None:
    """Test ep05 rag retrieves fixture."""
    assert run("receipt") == "doc-1"
