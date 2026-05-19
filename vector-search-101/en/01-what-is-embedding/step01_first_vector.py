import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
SENTENCES = [
    "Vector search starts by turning text into numbers.",
    "An embedding model places similar meanings close together.",
    "Let us inspect our first vector in Python.",
]


def main() -> None:
    model = SentenceTransformer(MODEL_NAME)
    vectors = model.encode(SENTENCES, normalize_embeddings=True, convert_to_numpy=True)

    print(f"Model: {MODEL_NAME}")
    print(f"Sentence count: {len(SENTENCES)}")
    print(f"Vector dimension: {vectors.shape[1]}")
    print()

    for index, (sentence, vector) in enumerate(
        zip(SENTENCES, vectors, strict=False), start=1
    ):
        print(f"[{index}] Sentence: {sentence}")
        print(f"    Vector norm: {np.linalg.norm(vector):.4f}")
        print(f"    First 5 values: {vector[:5].tolist()}")
        print()


if __name__ == "__main__":
    main()
