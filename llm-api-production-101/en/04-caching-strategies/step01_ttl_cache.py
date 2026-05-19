"""Llm Api Production 101 - Episode 1: Ttl cache."""

import hashlib
import json
import os
import time
from typing import Any, cast

from groq import Groq


class TTLCache:
    """TTL cache."""

    def __init__(self, ttl_seconds: int = 300) -> None:
        self._store: dict[str, tuple[str, float]] = {}
        self._ttl = ttl_seconds

    def _make_key(self, messages: list[dict], model: str) -> str:
        """Make key."""
        payload = json.dumps(
            {"model": model, "messages": messages}, ensure_ascii=False, sort_keys=True
        )
        return hashlib.sha256(payload.encode()).hexdigest()

    def get(self, messages: list[dict], model: str) -> str | None:
        """Get."""
        key = self._make_key(messages, model)
        entry = self._store.get(key)
        if entry is None:
            return None

        value, expiry = entry
        if time.monotonic() > expiry:
            del self._store[key]
            return None
        return value

    def set(self, messages: list[dict], model: str, value: str) -> None:
        """Set."""
        key = self._make_key(messages, model)
        self._store[key] = (value, time.monotonic() + self._ttl)


_cache = TTLCache(ttl_seconds=120)


def cached_chat(
    client: Groq, messages: list[dict], model: str = "llama-3.1-8b-instant"
) -> str:
    """Cached chat."""
    cached = _cache.get(messages, model)
    if cached is not None:
        print("[cache HIT]")
        return cached

    print("[cache MISS] Calling the API.")
    completion = client.chat.completions.create(
        model=model,
        messages=cast("Any", messages),
        temperature=0.0,
    )
    result = completion.choices[0].message.content or ""
    _cache.set(messages, model, result)
    return result


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    messages = [{"role": "user", "content": "Explain the Python GIL in one paragraph."}]

    started = time.monotonic()
    first = cached_chat(client, messages)
    print(f"1st call: {time.monotonic() - started:.3f}s")
    print(first[:100])

    started = time.monotonic()
    second = cached_chat(client, messages)
    print(f"\n2nd call: {time.monotonic() - started:.3f}s")
    assert first == second, "Cache hit check failed."
    print("TTL cache worked as expected.")


if __name__ == "__main__":
    main()
