"""Tests for ep04 in Multimodal Ai 101."""

from conftest import load_module

run = load_module("ko/04-captioning-ocr-pipelines/step01_caption_ocr.py", "ep04").run


def test_ep04_caption_and_ocr() -> None:
    """Test ep04 caption and ocr."""
    result = run()
    assert "caption" in result and "ocr" in result
    assert "total" in result["ocr"]
