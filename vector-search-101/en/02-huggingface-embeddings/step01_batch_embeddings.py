import numpy as np
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
PAIRS = [
    (
        "Vector search finds sentences with similar meaning.",
        "You can retrieve text whose meaning is close to the query.",
    ),
    (
        "Vector search finds sentences with similar meaning.",
        "I checked the baseball score this afternoon.",
    ),
    (
        "Chunking strategy has a big impact on retrieval quality.",
        "Search results change depending on how you split the document.",
    ),
]


def cosine_similarity(left: NDArray[np.float32], right: NDArray[np.float32]) -> float:
    return float(np.dot(left, right))


def main() -> None:
    model = SentenceTransformer(MODEL_NAME)
    flat_sentences = [sentence for pair in PAIRS for sentence in pair]
    embeddings = model.encode(
        flat_sentences, normalize_embeddings=True, convert_to_numpy=True
    )

    print(f"Model: {MODEL_NAME}")
    print(f"Sentences embedded in one batch: {len(flat_sentences)}")
    print()

    for pair_index, (sentence_a, sentence_b) in enumerate(PAIRS, start=0):
        vector_a = embeddings[pair_index * 2]
        vector_b = embeddings[pair_index * 2 + 1]
        similarity = cosine_similarity(vector_a, vector_b)

        print(f"Pair {pair_index + 1}")
        print(f"  A: {sentence_a}")
        print(f"  B: {sentence_b}")
        print(f"  Cosine similarity: {similarity:.4f}")
        print()


if __name__ == "__main__":
    main()
