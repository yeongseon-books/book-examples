from __future__ import annotations

import time

import numpy as np


def build_embeddings(texts: list[str], model_name: str) -> np.ndarray:
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(model_name)
    vectors = model.encode(texts, normalize_embeddings=True, convert_to_numpy=True)
    return np.asarray(vectors, dtype="float32")


def cosine_ranking(query_vector: np.ndarray, doc_vectors: np.ndarray, doc_ids: list[str], limit: int) -> list[str]:
    scores = np.dot(doc_vectors, query_vector)
    indices = np.argsort(scores)[::-1][:limit]
    return [doc_ids[index] for index in indices]


def timed_embeddings(texts: list[str], model_name: str) -> tuple[np.ndarray, float]:
    started = time.perf_counter()
    vectors = build_embeddings(texts, model_name)
    elapsed_ms = (time.perf_counter() - started) * 1000
    return vectors, elapsed_ms
