from common import MockOCR, MockVLM, synthetic_image


def run() -> dict[str, str]:
    image = synthetic_image(4)
    return {
        "caption": MockVLM().generate(image, "caption"),
        "ocr": MockOCR().extract("receipt", image),
    }
