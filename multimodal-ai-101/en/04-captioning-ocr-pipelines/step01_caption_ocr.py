"""Multimodal Ai 101 - Episode 4: captioning ocr pipelines example."""

from common import MockOCR, MockVLM, synthetic_image


def run() -> dict[str, str]:
    """Run."""
    image = synthetic_image(4)
    return {
        "caption": MockVLM().generate(image, "caption"),
        "ocr": MockOCR().extract("receipt", image),
    }
