"""Multimodal Ai 101 - Episode 2: image encoders clip vit example."""

from common import MockImageEncoder, synthetic_image


def run() -> dict[str, object]:
    """Run."""
    encoder = MockImageEncoder()
    vec = encoder.encode(synthetic_image(2))
    return {"dim": int(vec.shape[0]), "norm": float((vec**2).sum() ** 0.5)}
