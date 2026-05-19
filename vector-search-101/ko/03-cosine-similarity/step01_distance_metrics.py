"""Vector Search 101 - Episode 1: Distance metrics."""

import numpy as np
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
SENTENCES = [
    "FastAPI는 파이썬으로 API 서버를 빠르게 만드는 프레임워크입니다.",
    "Flask와 FastAPI는 모두 파이썬 웹 개발에 자주 사용됩니다.",
    "주말에는 산책하면서 사진을 찍는 것을 좋아합니다.",
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

    print(f"기준 문장: {SENTENCES[0]}")
    print()

    for sentence, vector in zip(SENTENCES[1:], vectors[1:], strict=False):
        print(f"비교 문장: {sentence}")
        print(f"  코사인 유사도: {cosine_similarity(query_vector, vector):.4f}")
        print(f"  유클리드 거리: {euclidean_distance(query_vector, vector):.4f}")
        print(f"  내적: {dot_product(query_vector, vector):.4f}")
        print()


if __name__ == "__main__":
    main()
