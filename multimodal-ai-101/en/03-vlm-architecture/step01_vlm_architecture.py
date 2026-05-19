from common import MockVLM, synthetic_image


def run(prompt: str = "describe") -> str:
    return MockVLM().generate(synthetic_image(3), prompt)
