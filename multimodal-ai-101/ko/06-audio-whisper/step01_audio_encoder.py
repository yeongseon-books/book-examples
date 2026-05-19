"""Multimodal Ai 101 - Episode 1: Audio encoder."""

from common import MockAudioEncoder, synthetic_audio


def run() -> float:
    """Run."""
    vec = MockAudioEncoder().encode(synthetic_audio())
    return float((vec**2).sum() ** 0.5)
