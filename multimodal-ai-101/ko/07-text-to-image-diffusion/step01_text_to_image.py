from common import MockDiffusion


def run(prompt: str = "cat") -> tuple[int, int]:
    img = MockDiffusion().generate(prompt, shape=(8, 8))
    return img.shape
