"""Generated from book-content article."""

import hashlib
import json
from typing import Optional

class ResponseCache:
    """LLM response cache."""

    def __init__(self, ttl_seconds: int = 3600):
        self._cache = {}
        self._ttl = ttl_seconds

    def _key(self, model: str, messages: list, temperature: float) -> str:
        payload = json.dumps({
            "model": model,
            "messages": messages,
            "temperature": temperature
        }, sort_keys=True)
        return hashlib.sha256(payload.encode()).hexdigest()

    def get(self, model: str, messages: list, temperature: float) -> Optional[str]:
        # temperature > 0 is unsafe to cache
        if temperature > 0:
            return None
        key = self._key(model, messages, temperature)
        entry = self._cache.get(key)
        if entry and time.time() - entry["timestamp"] < self._ttl:
            return entry["response"]
        return None

    def set(self, model: str, messages: list, temperature: float, response: str):
        if temperature > 0:
            return
        key = self._key(model, messages, temperature)
        self._cache[key] = {"response": response, "timestamp": time.time()}
