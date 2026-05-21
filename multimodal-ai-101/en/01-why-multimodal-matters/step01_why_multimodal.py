"""Multimodal Ai 101 - Episode 1: why multimodal matters example."""

from common import synthetic_image


def run() -> dict[str, object]:
    """Run."""
    image = synthetic_image(1)
    return {"shape": image.shape, "message": "multimodal combines modalities"}
