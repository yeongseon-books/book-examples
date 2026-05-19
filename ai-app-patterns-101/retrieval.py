from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


@dataclass
class RetrievedDocument:
    source: str
    content: str
    score: float


class SimpleVectorStore:
    def __init__(
        self,
        items: list[dict[str, str]],
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ) -> None:
        self.items = items
        self.encoder = SentenceTransformer(model_name)
        embeddings = self.encoder.encode(
            [item["content"] for item in items], normalize_embeddings=True
        )
        self.vectors = np.asarray(embeddings, dtype="float32")
        self.index: Any = faiss.IndexFlatIP(self.vectors.shape[1])
        self.index.add(self.vectors)

    def search(self, query: str, top_k: int = 2) -> list[RetrievedDocument]:
        query_vector = self.encoder.encode([query], normalize_embeddings=True)
        distances, indices = self.index.search(
            np.asarray(query_vector, dtype="float32"), top_k
        )
        results: list[RetrievedDocument] = []
        for score, idx in zip(distances[0], indices[0], strict=False):
            item = self.items[int(idx)]
            results.append(
                RetrievedDocument(
                    source=item["source"],
                    content=item["content"],
                    score=float(score),
                )
            )
        return results
