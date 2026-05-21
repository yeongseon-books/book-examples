"""Generated from book-content article."""

import json
from datetime import datetime
from typing import List, Dict, Optional

class LongTermMemory:
    """Long-term memory: permanently stored in external storage"""

    def __init__(self, storage_path: str = "memory.json"):
        self.storage_path = storage_path
        self.memories: Dict[str, List[Dict]] = self._load()

    def _load(self) -> Dict[str, List[Dict]]:
        """Load memory from storage"""
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
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

    def retrieve_memory(self, user_id: str, key: Optional[str] = None) -> List[Dict]:
        """Retrieve user's memory"""
        if user_id not in self.memories:
            return []

        memories = self.memories[user_id]

        if key:
                        # 반환: only memories matching the key
            return [m for m in memories if m["key"] == key]

        return memories
