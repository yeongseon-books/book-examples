from __future__ import annotations

import numpy as np
from common import cosine_similarity_matrix, embed_texts


class InMemoryVectorIndex:
    def __init__(self, dim: int = 128) -> None:
        self.dim = dim
        self.texts: list[str] = []
        self.matrix = np.zeros((0, dim), dtype=float)

    def add_texts(self, texts: list[str]) -> None:
        embs = embed_texts(texts, dim=self.dim)
        self.texts.extend(texts)
        self.matrix = np.vstack([self.matrix, embs]) if self.matrix.size else embs

    def search(self, query: str, top_k: int = 3) -> list[tuple[str, float]]:
        q = embed_texts([query], dim=self.dim)[0]
        scores = cosine_similarity_matrix(q, self.matrix)
        order = np.argsort(-scores)[:top_k]
        return [(self.texts[i], float(scores[i])) for i in order]
