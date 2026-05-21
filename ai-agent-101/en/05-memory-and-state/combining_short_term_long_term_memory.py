"""Generated from book-content article."""

class HybridMemory:
    """Short-term memory + long-term memory combined"""

    def __init__(self, user_id: str, system_prompt: str):
        self.user_id = user_id
        self.short_term = ShortTermMemory(system_prompt)
        self.long_term = LongTermMemory()

    def start_session(self):
        """Load relevant information from long-term memory on session start"""
        memories = self.long_term.retrieve_memory(self.user_id)

        if memories:
            # Add long-term memory content to system prompt
            context = "Previous user preferences:\n"
            for mem in memories:
                context += f"- {mem['key']}: {mem['value']}\n"

            self.short_term.messages[0]["content"] += f"\n\n{context}"

    def add_user_message(self, content: str):
        """Add user message"""
        self.short_term.add_user_message(content)

    def add_assistant_message(self, content: str):
        """Add agent response"""
        self.short_term.add_assistant_message(content)

    def save_important_info(self, key: str, value: str):
        """Save important information to long-term memory"""
        self.long_term.add_memory(self.user_id, key, value)

    def get_context(self) -> List[Dict[str, str]]:
        """Return current context"""
        return self.short_term.get_context()

    def end_session(self):
        """Session end: clear short-term memory"""
        self.short_term.clear()

# Usage example
memory = HybridMemory(user_id="user123", system_prompt="You are a helpful assistant.")

# Start session: Load previous information from long-term memory
memory.start_session()

# Conversation
memory.add_user_message("Tell me about AI Agents")
memory.add_assistant_message("AI Agents are systems that autonomously perform tasks using LLMs.")

# Save important information to long-term memory
memory.save_important_info("last_topic", "AI Agent")

# End session
memory.end_session()

# Next session will automatically load "last_topic: AI Agent"
