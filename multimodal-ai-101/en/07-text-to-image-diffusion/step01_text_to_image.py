"""Multimodal Ai 101 - Episode 7: text to image diffusion example."""

from common import MockDiffusion


def run(prompt: str = "cat") -> tuple[int, int]:
    """Run."""
    img = MockDiffusion().generate(prompt, shape=(8, 8))
    return img.shape
