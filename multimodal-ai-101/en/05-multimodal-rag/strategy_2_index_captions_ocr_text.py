"""Generated from book-content article."""

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("BAAI/bge-base-en-v1.5")

def index_text(items: list[dict]):
    texts = [f"{it['caption']}\n\n{it['ocr_text']}" for it in items]
    vecs = embedder.encode(texts, normalize_embeddings=True).astype("float32")
    index = faiss.IndexFlatIP(vecs.shape[1])
    index.add(vecs)
    return index, items

# Assumes caption / ocr_text are precomputed per image
items = [
    {"path": "slides/01.png",
     "caption": "bar chart of revenue",
     "ocr_text": "Q1: 1.2M Q2: 1.5M Q3: 0.9M"},
    # ...
]
index, items = index_text(items)

def search(q: str, k: int = 3):
    qv = embedder.encode([q], normalize_embeddings=True).astype("float32")
    D, I = index.search(qv, k=k)
    return [items[i] for i in I[0]]

for r in search("Q3 revenue dropped"):
    print(r["path"], r["caption"])
