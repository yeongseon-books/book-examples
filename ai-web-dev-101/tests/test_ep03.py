"""Tests for ep03 in Ai Web Dev 101."""

from conftest import load_module

ChatSession = load_module("ko/03-ai-chatbot/step01_chat_state.py", "ep03").ChatSession


def test_ep03_chat_state_accumulates_messages() -> None:
    """Test ep03 chat state accumulates messages."""
    chat = ChatSession(system_prompt="친절한 요리 도우미")
    answer = chat.send("감자 요리 추천")
    assert len(chat.messages) == 2
    assert "요리 도우미" in answer
