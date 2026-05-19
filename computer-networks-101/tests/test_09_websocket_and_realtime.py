"""Tests for 09 websocket and realtime in Computer Networks 101."""

from tests._loader import load_ko


def test_websocket_frame_roundtrip() -> None:
    """Test websocket frame roundtrip."""
    ep = load_ko("09-websocket-and-realtime")
    frame = ep.encode_masked_text_frame("hello")
    parsed = ep.parse_websocket_frame(frame)
    assert parsed["fin"] is True
    assert parsed["opcode"] == 1
    assert parsed["payload"] == "hello"
