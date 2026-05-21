# pip install sentence-transformers faiss-cpu
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


def semantic_dedup(docs: list[str], threshold: float = 0.93) -> list[str]:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embs = model.encode(docs, normalize_embeddings=True).astype("float32")
    index = faiss.IndexFlatIP(embs.shape[1])  # inner product = cosine on normalized
    keep: list[int] = []
    for i, e in enumerate(embs):
        if index.ntotal > 0:
            scores, _ = index.search(e.reshape(1, -1), 1)
            if scores[0][0] >= threshold:
                continue  # near-paraphrase, skip
        index.add(e.reshape(1, -1))
        keep.append(i)
    return [docs[i] for i in keep]
