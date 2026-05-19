"""Tests for ep02 in Multimodal Ai 101."""

from common import MockImageEncoder, synthetic_image


def test_ep02_image_encoder_deterministic() -> None:
    """Test ep02 image encoder deterministic."""
    encoder = MockImageEncoder()
    a = encoder.encode(synthetic_image(2))
    b = encoder.encode(synthetic_image(2))
    assert (a == b).all()
