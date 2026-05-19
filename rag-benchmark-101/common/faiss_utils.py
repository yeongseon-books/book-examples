from __future__ import annotations

import time

import faiss
import numpy as np


def build_faiss_index(vectors: np.ndarray, factory: str):
    vectors32 = np.ascontiguousarray(vectors, dtype="float32")
    dimension = vectors32.shape[1]
    if factory == "Flat":
        index = faiss.IndexFlatIP(dimension)
    elif factory == "HNSW32":
        index = faiss.IndexHNSWFlat(dimension, 32)
        index.metric_type = faiss.METRIC_INNER_PRODUCT
    elif factory == "IVF32,Flat":
        quantizer = faiss.IndexFlatIP(dimension)
        index = faiss.IndexIVFFlat(quantizer, dimension, 32, faiss.METRIC_INNER_PRODUCT)
        index.train(vectors32)  # pyright: ignore[reportCallIssue]
        index.nprobe = 8
    else:
        raise ValueError(f"Unsupported FAISS factory: {factory}")
    index.add(vectors32)  # pyright: ignore[reportCallIssue]
    return index


def faiss_search(
    index, query_vectors: np.ndarray, doc_ids: list[str], limit: int
) -> tuple[list[list[str]], float]:
    queries32 = np.ascontiguousarray(query_vectors, dtype="float32")
    started = time.perf_counter()
    _, indices = index.search(queries32, limit)
    elapsed_ms = (time.perf_counter() - started) * 1000
    ranked_ids = [[doc_ids[i] for i in row if i >= 0] for row in indices.tolist()]
    return ranked_ids, elapsed_ms
