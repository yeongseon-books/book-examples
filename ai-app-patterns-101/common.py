from __future__ import annotations

import os
from typing import Any, Iterable, cast

from groq import Groq

DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")


def build_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set.")
    return Groq(api_key=api_key)


def response_text(message: Any) -> str:
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
    print(f"\n{'=' * 12} {title} {'=' * 12}")


def as_messages(messages: list[dict[str, Any]]) -> Any:
    return cast(Any, messages)


def as_tools(tools: list[dict[str, Any]]) -> Any:
    return cast(Any, tools)
