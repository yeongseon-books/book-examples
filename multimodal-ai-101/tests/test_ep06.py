"""Tests for ep06 in Multimodal Ai 101."""

from conftest import load_module

run = load_module("ko/06-audio-whisper/step01_audio_encoder.py", "ep06").run


def test_ep06_audio_encoder_norm() -> None:
    """Test ep06 audio encoder norm."""
    assert abs(run() - 1.0) < 1e-6
