"""Multimodal Ai 101 - Episode 3: vlm architecture example."""

from common import MockVLM, synthetic_image


def run(prompt: str = "describe") -> str:
    """Run."""
    return MockVLM().generate(synthetic_image(3), prompt)
