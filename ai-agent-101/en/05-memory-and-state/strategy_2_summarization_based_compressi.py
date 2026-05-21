"""Generated from book-content article."""

from openai import OpenAI
from typing import List, Dict

class SummarizationMemory:
    """Summarization-based memory: summarize old conversations"""
    
    def __init__(self, system_prompt: str, api_key: str, max_messages: int = 10):
        self.system_prompt = system_prompt
        self.max_messages = max_messages
        self.client = OpenAI(api_key=api_key)
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]
        self.summary: str = ""
    
    def _summarize(self, messages: List[Dict[str, str]]) -> str:
        """Summarize conversation content"""
        conversation = "\n".join([
            f"{msg['role']}: {msg['content']}" for msg in messages if msg['role'] != 'system'
        ])
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize the following conversation in 2-3 sentences."},
                {"role": "user", "content": conversation}
            ],
            temperature=0
        )
        
        return response.choices[0].message.content
    
    def add_message(self, role: str, content: str):
        """Add message"""
        self.messages.append({"role": role, "content": content})
        
        # Summarize when messages grow too large
        if len(self.messages) - 1 > self.max_messages:
            # Summarize first half (excluding system prompt)
            to_summarize = self.messages[1:self.max_messages//2 + 1]
            new_summary = self._summarize(to_summarize)
            
            # Combine with existing summary
            if self.summary:
                self.summary += f"\n\n{new_summary}"
            else:
                self.summary = new_summary
            
            # Remove summarized portion
            self.messages = [self.messages[0]] + self.messages[self.max_messages//2 + 1:]
    
    def get_context(self) -> List[Dict[str, str]]:
        """Return current context (including summary)"""
        system_content = self.system_prompt
        
        if self.summary:
            system_content += f"\n\nPrevious conversation summary:\n{self.summary}"
        
        return [
            {"role": "system", "content": system_content}
        ] + self.messages[1:]

# Usage example
memory = SummarizationMemory(
    system_prompt="You are a helpful assistant.",
    api_key="your-api-key",
    max_messages=6
)

memory.add_message("user", "How to do web scraping in Python?")
memory.add_message("assistant", "Use requests and BeautifulSoup libraries...")
memory.add_message("user", "Show me example code")
memory.add_message("assistant", "Here's an example: import requests...")
memory.add_message("user", "How about error handling?")
memory.add_message("assistant", "Handle with try-except...")
memory.add_message("user", "Different question: How to use FastAPI?")  
# At this point, web scraping conversation gets summarized, only recent conversation retained

context = memory.get_context()
print(f"Summary: {memory.summary[:100]}...")  # "User asked about web scraping in Python..."
