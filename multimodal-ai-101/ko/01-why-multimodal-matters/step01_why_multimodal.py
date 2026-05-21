"""Multimodal Ai 101 - 1편: why multimodal matters 예제."""

from common import synthetic_image


def run() -> dict[str, object]:
    """Run."""
    image = synthetic_image(1)
    return {"shape": image.shape, "message": "multimodal combines modalities"}
