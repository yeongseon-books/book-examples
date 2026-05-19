"""Vector Search 101 - Episode 1: Chunking and search."""

import faiss
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DOCUMENT = (
    "A vector search system usually splits a long document into smaller chunks before embedding it. "
    "If a chunk is too large, unrelated topics get mixed together, and if it is too small, the context breaks apart. "
    "Fixed-size chunking is simple to implement, so it is a good first experiment. "
    "Adding overlap helps recover context that was cut at the chunk boundary. "
    "During retrieval, the system finds the chunk whose meaning is closest to the question."
)


def fixed_size_chunks(text: str, size: int, overlap: int) -> list[str]:
    """Fixed size chunks."""
    words = text.split()
    step = size - overlap
    if step <= 0:
        raise ValueError("overlap must be smaller than size")

    chunks: list[str] = []
    for start in range(0, len(words), step):
        chunk = " ".join(words[start : start + size])
        if chunk:
            chunks.append(chunk)
    return chunks


def main() -> None:
    """Main."""
    model = SentenceTransformer(MODEL_NAME)
    query = "How can I split chunks without losing too much context?"

    for size, overlap in [(12, 3), (20, 5)]:
        chunks = fixed_size_chunks(DOCUMENT, size=size, overlap=overlap)
        vectors = model.encode(
            chunks, normalize_embeddings=True, convert_to_numpy=True
        ).astype("float32")
        index = faiss.IndexFlatIP(vectors.shape[1])
        index.add(vectors)  # pyright: ignore[reportCallIssue]

        query_vector = model.encode(
            [query], normalize_embeddings=True, convert_to_numpy=True
        ).astype("float32")
        scores, indices = index.search(query_vector, 2)  # pyright: ignore[reportCallIssue]

        print(f"size={size}, overlap={overlap}, chunk_count={len(chunks)}")
        for rank, (chunk_index, score) in enumerate(
            zip(indices[0], scores[0], strict=False), start=1
        ):
            preview = chunks[int(chunk_index)]
            print(f"  {rank}. score={float(score):.4f} | {preview}")
        print()


if __name__ == "__main__":
    main()
