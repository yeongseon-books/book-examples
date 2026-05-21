"""Generated from book-content article."""

import sqlite3
from typing import Optional, List, Dict
from datetime import datetime

class StructuredMemoryStore:
    """General DB-based structured memory"""
    
    def __init__(self, db_path: str = "memory.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()
    
    def _init_db(self):
        """Create tables"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_preferences (
                user_id TEXT,
                key TEXT,
                value TEXT,
                updated_at TEXT,
                PRIMARY KEY (user_id, key)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversation_summary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                session_id TEXT,
                summary TEXT,
                created_at TEXT
            )
        """)
        self.conn.commit()
    
    def set_preference(self, user_id: str, key: str, value: str):
        """Save user preference"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO user_preferences (user_id, key, value, updated_at)
            VALUES (?, ?, ?, ?)
        """, (user_id, key, value, datetime.now().isoformat()))
        self.conn.commit()
    
    def get_preference(self, user_id: str, key: str) -> Optional[str]:
        """Retrieve user preference"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT value FROM user_preferences
            WHERE user_id = ? AND key = ?
        """, (user_id, key))
        
        result = cursor.fetchone()
        return result[0] if result else None
    
    def get_all_preferences(self, user_id: str) -> Dict[str, str]:
        """Retrieve all user preferences"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT key, value FROM user_preferences
            WHERE user_id = ?
        """, (user_id,))
        
        return {row[0]: row[1] for row in cursor.fetchall()}
    
    def save_session_summary(self, user_id: str, session_id: str, summary: str):
        """Save session summary"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO conversation_summary (user_id, session_id, summary, created_at)
            VALUES (?, ?, ?, ?)
        """, (user_id, session_id, summary, datetime.now().isoformat()))
        self.conn.commit()
    
    def get_recent_summaries(self, user_id: str, limit: int = 5) -> List[Dict]:
        """Retrieve recent session summaries"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT session_id, summary, created_at
            FROM conversation_summary
            WHERE user_id = ?
            ORDER BY created_at DESC
            LIMIT ?
        """, (user_id, limit))
        
        return [
            {"session_id": row[0], "summary": row[1], "created_at": row[2]}
            for row in cursor.fetchall()
        ]

# Usage example
db_store = StructuredMemoryStore()

# Save user preferences
db_store.set_preference("user123", "language", "Korean")
db_store.set_preference("user123", "notification", "enabled")

# Retrieve
lang = db_store.get_preference("user123", "language")
print(f"Preferred language: {lang}")  # Korean

all_prefs = db_store.get_all_preferences("user123")
print(f"All settings: {all_prefs}")

# Save session summary
db_store.save_session_summary(
    user_id="user123",
    session_id="sess_001",
    summary="User asked about Python web scraping and was guided on BeautifulSoup usage."
)

# Retrieve recent conversation summaries
recent = db_store.get_recent_summaries("user123", limit=3)
print(f"Recent conversations: {recent}")
