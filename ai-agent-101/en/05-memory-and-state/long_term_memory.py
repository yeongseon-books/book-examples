"""Generated from book-content article."""

import json
from datetime import datetime
from typing import Dict, List, Optional


class LongTermMemory:
    """Long-term memory: permanently stored in external storage"""

    def __init__(self, storage_path: str = "memory.json"):
        self.storage_path = storage_path
        self.memories: dict[str, list[dict]] = self._load()

    def _load(self) -> dict[str, list[dict]]:
        """Load memory from storage"""
        try:
            with open(self.storage_path, encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save(self):
        """Save memory to storage"""
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.memories, f, ensure_ascii=False, indent=2)

    def add_memory(self, user_id: str, key: str, value: str):
        """Add information to user's memory"""
        if user_id not in self.memories:
            self.memories[user_id] = []

        self.memories[user_id].append({
            "key": key,
            "value": value,
            "timestamp": datetime.now().isoformat()
        })
        self._save()

    def retrieve_memory(self, user_id: str, key: str | None = None) -> list[dict]:
        """Retrieve user's memory"""
        if user_id not in self.memories:
            return []

        memories = self.memories[user_id]

        if key:
            # Return only memories matching the key
            return [m for m in memories if m["key"] == key]

        return memories

# Usage example
long_memory = LongTermMemory()

# Session 1: Save user preferences
long_memory.add_memory(
    user_id="user123",
    key="language_preference",
    value="Korean"
)
long_memory.add_memory(
    user_id="user123",
    key="topic_interest",
    value="AI Agent"
)

# Session 2 (later reconnection): Retrieve previous information
preferences = long_memory.retrieve_memory(user_id="user123")
print(f"User preferences: {preferences}")
# [{'key': 'language_preference', 'value': 'Korean', 'timestamp': '...'}, ...]

# Retrieve specific key only
lang_pref = long_memory.retrieve_memory(user_id="user123", key="language_preference")
if lang_pref:
    print(f"Preferred language: {lang_pref[0]['value']}")  # Korean
