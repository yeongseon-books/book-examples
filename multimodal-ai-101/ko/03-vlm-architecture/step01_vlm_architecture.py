"""Multimodal Ai 101 - Episode 1: Vlm architecture."""

from common import MockVLM, synthetic_image


def run(prompt: str = "describe") -> str:
    """Run."""
    return MockVLM().generate(synthetic_image(3), prompt)
