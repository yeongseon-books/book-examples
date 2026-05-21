"""Generated from book-content article."""

import numpy as np
from openai import OpenAI

client = OpenAI()
SIMILARITY_THRESHOLD = 0.82

def embed(text: str) -> np.ndarray:
    resp = client.embeddings.create(model="text-embedding-3-small", input=text)
    v = np.array(resp.data[0].embedding)
    return v / np.linalg.norm(v)

# Build once at startup; in production back this with FAISS or pgvector
JAILBREAK_INDEX = np.stack([embed(p) for p in load_jailbreak_dataset()])

def embedding_score(text: str) -> float:
    q = embed(text)
    return float((JAILBREAK_INDEX @ q).max())

def is_jailbreak_by_embedding(text: str) -> bool:
    return embedding_score(text) >= SIMILARITY_THRESHOLD
