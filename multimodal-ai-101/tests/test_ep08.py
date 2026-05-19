"""Tests for ep08 in Multimodal Ai 101."""

from common import MockTextEncoder


def test_ep08_text_encoder_separation() -> None:
    """Test ep08 text encoder separation."""
    encoder = MockTextEncoder()
    a = encoder.encode("cat")
    b = encoder.encode("dog")
    assert not (a == b).all()
