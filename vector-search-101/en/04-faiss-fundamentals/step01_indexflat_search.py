"""Vector Search 101 - Episode 1: Indexflat search."""

import faiss
import numpy as np
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CORPUS = [
    "Embeddings convert text into numeric vectors.",
    "FAISS is a library for fast similarity search over large vector sets.",
    "FastAPI is often used to build Python API servers.",
    "Chunking splits a long document into smaller searchable pieces.",
    "Cosine similarity measures how closely two vectors point in the same direction.",
    "A vector database is optimized for storing and querying embeddings.",
]


def build_index(
    model: SentenceTransformer, corpus: list[str]
) -> tuple[faiss.IndexFlatIP, NDArray[np.float32]]:
    """Build index."""
    vectors = model.encode(
        corpus, normalize_embeddings=True, convert_to_numpy=True
    ).astype("float32")
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)  # pyright: ignore[reportCallIssue]
    return index, vectors


def search(
    model: SentenceTransformer,
    index: faiss.IndexFlatIP,
    query: str,
    top_k: int = 3,
) -> list[tuple[int, float]]:
    """Search."""
    query_vector = model.encode(
        [query], normalize_embeddings=True, convert_to_numpy=True
    ).astype("float32")
    scores, indices = index.search(query_vector, top_k)  # pyright: ignore[reportCallIssue]
    return list(zip(indices[0].tolist(), scores[0].tolist(), strict=False))


def main() -> None:
    """Main."""
    model = SentenceTransformer(MODEL_NAME)
    index, vectors = build_index(model, CORPUS)

    print(f"Document count: {len(CORPUS)}")
    print(f"Vector dimension: {vectors.shape[1]}")
    print()

    queries = [
        "I want a library for vector similarity search.",
        "I want to build a Python API server.",
    ]

    for query in queries:
        print(f"Query: {query}")
        for rank, (doc_index, score) in enumerate(search(model, index, query), start=1):
            print(f"  {rank}. score={score:.4f} | {CORPUS[doc_index]}")
        print()


if __name__ == "__main__":
    main()
