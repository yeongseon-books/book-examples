"""Shared utilities and domain models for Ai App Patterns 101."""

from __future__ import annotations

import os
from collections.abc import Iterable
from typing import Any, cast

from groq import Groq

DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")


def build_client() -> Groq:
    """Build client."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set.")
    return Groq(api_key=api_key)


def response_text(message: Any) -> str:
    """Response text."""
    content = getattr(message, "content", "")
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, Iterable):
        parts: list[str] = []
        for item in content:
            text = getattr(item, "text", None)
            if text:
                parts.append(text)
        return "\n".join(parts).strip()
    return ""


def print_section(title: str) -> None:
    """Print section."""
    print(f"\n{'=' * 12} {title} {'=' * 12}")


def as_messages(messages: list[dict[str, Any]]) -> Any:
    """As messages."""
    return cast("Any", messages)


def as_tools(tools: list[dict[str, Any]]) -> Any:
    """As tools."""
    return cast("Any", tools)
