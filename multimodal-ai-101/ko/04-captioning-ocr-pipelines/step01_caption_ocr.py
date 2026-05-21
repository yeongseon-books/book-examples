"""Multimodal Ai 101 - 4편: captioning ocr pipelines 예제."""

from common import MockOCR, MockVLM, synthetic_image


def run() -> dict[str, str]:
    """Run."""
    image = synthetic_image(4)
    return {
        "caption": MockVLM().generate(image, "caption"),
        "ocr": MockOCR().extract("receipt", image),
    }
