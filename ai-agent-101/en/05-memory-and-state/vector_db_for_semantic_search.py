"""Generated from book-content article."""

from openai import OpenAI
from typing import List, Dict
import numpy as np
from datetime import datetime

class VectorMemoryStore:
    """Vector DB-based long-term memory"""
    
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.memories: List[Dict] = []  # Use Pinecone, Weaviate, etc. in practice
    
    def _get_embedding(self, text: str) -> List[float]:
        """Convert text to embedding vector"""
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    
    def add_memory(self, user_id: str, content: str, metadata: Dict = None):
        """Add memory (convert to vector and store)"""
        embedding = self._get_embedding(content)
        
        memory = {
            "user_id": user_id,
            "content": content,
            "embedding": embedding,
            "metadata": metadata or {},
            "timestamp": datetime.now().isoformat()
        }
        
        self.memories.append(memory)
    
    def search_memory(self, user_id: str, query: str, top_k: int = 3) -> List[Dict]:
        """Similarity-based memory search"""
        query_embedding = self._get_embedding(query)
        
        # Filter to user's memories only
        user_memories = [m for m in self.memories if m["user_id"] == user_id]
        
        if not user_memories:
            return []
        
        # Calculate cosine similarity
        similarities = []
        for memory in user_memories:
            similarity = self._cosine_similarity(query_embedding, memory["embedding"])
            similarities.append((memory, similarity))
        
        # Sort by similarity (descending)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Return top k
        return [{"content": m["content"], "similarity": sim} for m, sim in similarities[:top_k]]
    
    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calculate cosine similarity"""
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Usage example
memory_store = VectorMemoryStore(api_key="your-api-key")

# Store past conversations
memory_store.add_memory(
    user_id="user123",
    content="User asked about web scraping in Python, recommended BeautifulSoup.",
    metadata={"topic": "web_scraping"}
)
memory_store.add_memory(
    user_id="user123",
    content="User asked about building REST API with FastAPI.",
    metadata={"topic": "fastapi"}
)

# Search for past information related to current question
query = "Tell me about Python web crawling"
relevant_memories = memory_store.search_memory(user_id="user123", query=query, top_k=2)

print("Related past conversations:")
for mem in relevant_memories:
    print(f"- {mem['content']} (similarity: {mem['similarity']:.2f})")

# "web scraping" conversation retrieved with high similarity
