"""Shared utilities and domain models for Rag Deep Dive."""

from __future__ import annotations

import hashlib
from collections.abc import Iterable
from pathlib import Path

import numpy as np


def sentence_split(text: str) -> list[str]:
    """Sentence split."""
    parts = [p.strip() for p in text.replace("\n", " ").split(".")]
    return [p + "." for p in parts if p]


def deterministic_vector(text: str, dim: int = 128) -> np.ndarray:
    """Deterministic vector."""
    seed_bytes = hashlib.sha256(text.encode("utf-8")).digest()[:8]
    seed = int.from_bytes(seed_bytes, "big", signed=False)
    rng = np.random.default_rng(seed)
    vec = rng.normal(0.0, 1.0, size=dim)
    norm = np.linalg.norm(vec)
    return vec / (norm if norm > 0 else 1.0)


def embed_texts(texts: Iterable[str], dim: int = 128) -> np.ndarray:
    """Embed texts."""
    vectors = [deterministic_vector(t, dim=dim) for t in texts]
    if not vectors:
        return np.zeros((0, dim), dtype=float)
    return np.vstack(vectors)


def cosine_similarity_matrix(query_vec: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """Cosine similarity matrix."""
    if matrix.size == 0:
        return np.array([], dtype=float)
    qn = np.linalg.norm(query_vec)
    q = query_vec / (qn if qn > 0 else 1.0)
    mn = np.linalg.norm(matrix, axis=1, keepdims=True)
    m = matrix / np.where(mn > 0, mn, 1.0)
    return m @ q


def mock_llm_answer(question: str, contexts: list[str]) -> str:
    """Mock llm answer."""
    joined = " | ".join(contexts[:3])
    return (
        "[MOCK_ANSWER]\n"
        f"Q: {question}\n"
        f"A: Based on retrieved context: {joined}\n"
        "This is a deterministic offline mock response."
    )


def load_markdown_fixtures(fixtures_dir: str | Path) -> dict[str, str]:
    """Load markdown fixtures."""
    root = Path(fixtures_dir)
    docs: dict[str, str] = {}
    for path in sorted(root.glob("*.md")):
        docs[path.name] = path.read_text(encoding="utf-8")
    return docs
