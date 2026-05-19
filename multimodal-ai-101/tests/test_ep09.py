"""Tests for ep09 in Multimodal Ai 101."""

from conftest import load_module

run = load_module("ko/09-video-understanding/step01_video_understanding.py", "ep09").run


def test_ep09_video_pooling_vector_dim() -> None:
    """Test ep09 video pooling vector dim."""
    assert run() == 512
