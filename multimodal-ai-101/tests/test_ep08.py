from common import MockTextEncoder


def test_ep08_text_encoder_separation() -> None:
    encoder = MockTextEncoder()
    a = encoder.encode("cat")
    b = encoder.encode("dog")
    assert not (a == b).all()
