"""Vector Search 101 - Episode 1: Distance metrics."""

import numpy as np
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
SENTENCES = [
    "FastAPI is a framework for building Python API servers quickly.",
    "Flask and FastAPI are both common choices for Python web development.",
    "I like taking photos while walking on the weekend.",
]


def cosine_similarity(left: NDArray[np.float32], right: NDArray[np.float32]) -> float:
    """Cosine similarity."""
    return float(np.dot(left, right))


def euclidean_distance(left: NDArray[np.float32], right: NDArray[np.float32]) -> float:
    """Euclidean distance."""
    return float(np.linalg.norm(left - right))


def dot_product(left: NDArray[np.float32], right: NDArray[np.float32]) -> float:
    """Dot product."""
    return float(np.dot(left, right))


def main() -> None:
    """Main."""
    model = SentenceTransformer(MODEL_NAME)
    vectors = model.encode(SENTENCES, normalize_embeddings=True, convert_to_numpy=True)
    query_vector = vectors[0]

    print(f"Reference sentence: {SENTENCES[0]}")
    print()

    for sentence, vector in zip(SENTENCES[1:], vectors[1:], strict=False):
        print(f"Compared sentence: {sentence}")
        print(f"  Cosine similarity: {cosine_similarity(query_vector, vector):.4f}")
        print(f"  Euclidean distance: {euclidean_distance(query_vector, vector):.4f}")
        print(f"  Dot product: {dot_product(query_vector, vector):.4f}")
        print()


if __name__ == "__main__":
    main()
