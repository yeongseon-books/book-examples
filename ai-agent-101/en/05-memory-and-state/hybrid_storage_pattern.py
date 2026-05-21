"""Generated from book-content article."""

class HybridMemorySystem:
    """Vector DB + general DB combined"""

    def __init__(self, api_key: str, db_path: str = "memory.db"):
        self.vector_store = VectorMemoryStore(api_key=api_key)
        self.structured_store = StructuredMemoryStore(db_path=db_path)

    def initialize_user_context(self, user_id: str, query: str) -> str:
        """Initialize user context (load long-term memory)"""
        context_parts = []

        # 1. Load structured preferences
        preferences = self.structured_store.get_all_preferences(user_id)
        if preferences:
            context_parts.append("User Preferences:")
            for key, value in preferences.items():
                context_parts.append(f"- {key}: {value}")

        # 2. Load recent session summaries
        recent_summaries = self.structured_store.get_recent_summaries(user_id, limit=3)
        if recent_summaries:
            context_parts.append("\nRecent Conversations:")
            for summary in recent_summaries:
                context_parts.append(f"- {summary['summary']}")

        # 3. Search past conversations related to current question
        relevant_memories = self.vector_store.search_memory(user_id, query, top_k=2)
        if relevant_memories:
            context_parts.append("\nRelevant Past Discussions:")
            for mem in relevant_memories:
                context_parts.append(f"- {mem['content']}")

        return "\n".join(context_parts)

    def save_conversation(self, user_id: str, session_id: str, messages: List[Dict]):
        """Save on conversation end"""
        # 1. Generate conversation summary (use LLM in practice)
        summary = f"Discussed {len(messages)} topics"
        self.structured_store.save_session_summary(user_id, session_id, summary)

        # 2. Save important conversations to vector DB
        for msg in messages:
            if msg["role"] == "user" and len(msg["content"]) > 50:
                self.vector_store.add_memory(
                    user_id=user_id,
                    content=msg["content"],
                    metadata={"session_id": session_id}
                )

# Usage example
hybrid_system = HybridMemorySystem(api_key="your-api-key")

# Session start: Load long-term memory
user_context = hybrid_system.initialize_user_context(
    user_id="user123",
    query="Tell me about Python data analysis"
)

print("User Context:")
print(user_context)
# Output:
# User Preferences:
# - language: Korean
# Recent Conversations:
# - User asked about Python web scraping...
# Relevant Past Discussions:
# - Data analysis using Python pandas...

# Add this context to system prompt and pass to agent
