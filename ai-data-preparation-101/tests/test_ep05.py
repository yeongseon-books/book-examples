"""Tests for ep05 in Ai Data Preparation 101."""

from conftest import run_dict


def test_ep05_chunk() -> None:
    """Test ep05 chunk."""
    result = run_dict("ko/05-tokenization-chunking/step01_token_chunk.py")
    assert int(result["tokens"]) >= int(result["first_chunk_size"])
    assert int(result["chunks"]) >= 2
