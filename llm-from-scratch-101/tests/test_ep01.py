"""Tests for ep01 in Llm From Scratch 101."""

from common import CharTokenizer


def test_tokenizer_roundtrip() -> None:
    """Test tokenizer roundtrip."""
    tok = CharTokenizer("abc xyz")
    ids = tok.encode("cab")
    assert tok.decode(ids) == "cab"
