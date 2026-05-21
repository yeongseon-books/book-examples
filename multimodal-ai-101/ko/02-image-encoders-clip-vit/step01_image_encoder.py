"""Multimodal Ai 101 - 2편: image encoders clip vit 예제."""

from common import MockImageEncoder, synthetic_image


def run() -> dict[str, object]:
    """Run."""
    encoder = MockImageEncoder()
    vec = encoder.encode(synthetic_image(2))
    return {"dim": int(vec.shape[0]), "norm": float((vec**2).sum() ** 0.5)}
