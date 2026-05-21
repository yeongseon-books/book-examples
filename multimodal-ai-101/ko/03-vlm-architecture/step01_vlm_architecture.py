"""Multimodal Ai 101 - 3편: vlm architecture 예제."""

from common import MockVLM, synthetic_image


def run(prompt: str = "describe") -> str:
    """Run."""
    return MockVLM().generate(synthetic_image(3), prompt)
