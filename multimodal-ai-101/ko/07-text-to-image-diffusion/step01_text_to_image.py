"""Multimodal Ai 101 - 7편: text to image diffusion 예제."""

from common import MockDiffusion


def run(prompt: str = "cat") -> tuple[int, int]:
    """Run."""
    img = MockDiffusion().generate(prompt, shape=(8, 8))
    return img.shape
