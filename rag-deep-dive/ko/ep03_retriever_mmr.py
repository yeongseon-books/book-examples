from __future__ import annotations

import numpy as np
from common import cosine_similarity_matrix, embed_texts


def top_k_retrieve(
    query: str, chunks: list[str], top_k: int = 3, dim: int = 128
) -> list[tuple[int, str, float]]:
    matrix = embed_texts(chunks, dim=dim)
    q = embed_texts([query], dim=dim)[0]
    scores = cosine_similarity_matrix(q, matrix)
    order = np.argsort(-scores)[:top_k]
    return [(int(i), chunks[i], float(scores[i])) for i in order]


def mmr_rerank(
    query: str,
    chunks: list[str],
    top_k: int = 3,
    lambda_mult: float = 0.7,
    dim: int = 128,
) -> list[tuple[int, str, float]]:
    matrix = embed_texts(chunks, dim=dim)
    q = embed_texts([query], dim=dim)[0]
    rel = cosine_similarity_matrix(q, matrix)
    selected: list[int] = []
    candidates = set(range(len(chunks)))

    while candidates and len(selected) < top_k:
        best_i = None
        best_score = -1e9
        for i in candidates:
            div_penalty = 0.0
            if selected:
                sim_to_sel = [float(matrix[i] @ matrix[j]) for j in selected]
                div_penalty = max(sim_to_sel)
            score = lambda_mult * float(rel[i]) - (1 - lambda_mult) * div_penalty
            if score > best_score:
                best_score = score
                best_i = i
        assert best_i is not None
        selected.append(best_i)
        candidates.remove(best_i)

    return [(i, chunks[i], float(rel[i])) for i in selected]
