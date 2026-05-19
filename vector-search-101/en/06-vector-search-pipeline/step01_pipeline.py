import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DOCUMENTS = [
    "An embedding model converts text into fixed-length vectors.",
    "Cosine similarity compares the direction of a query vector and a document vector.",
    "FAISS IndexFlatIP is a simple starting point for searching normalized vectors.",
    "Fixed-size chunking is the most straightforward way to split a long document.",
    "A vector search pipeline usually has ingestion, chunking, embedding, indexing, and retrieval steps.",
    "Retrieved chunks can be passed to a later answer generation stage.",
]


class VectorSearchPipeline:
    def __init__(self, model_name: str = MODEL_NAME) -> None:
        self._model = SentenceTransformer(model_name)
        self._index: faiss.IndexFlatIP | None = None
        self._documents: list[str] = []

    def build(self, documents: list[str]) -> None:
        self._documents = documents
        vectors = self._model.encode(documents, normalize_embeddings=True, convert_to_numpy=True).astype("float32")
        self._index = faiss.IndexFlatIP(vectors.shape[1])
        self._index.add(vectors)  # pyright: ignore[reportCallIssue]
        print(f"Index built: {len(documents)} documents, dimension {vectors.shape[1]}")

    def search(self, query: str, top_k: int = 3) -> list[dict[str, float | str]]:
        if self._index is None:
            raise RuntimeError("Call build() first.")

        query_vector = self._model.encode([query], normalize_embeddings=True, convert_to_numpy=True).astype("float32")
        scores, indices = self._index.search(query_vector, top_k)  # pyright: ignore[reportCallIssue]

        results: list[dict[str, float | str]] = []
        for doc_index, score in zip(indices[0], scores[0], strict=False):
            results.append(
                {
                    "score": float(score),
                    "text": self._documents[int(doc_index)],
                }
            )
        return results


def main() -> None:
    pipeline = VectorSearchPipeline()
    pipeline.build(DOCUMENTS)

    for query in [
        "What steps make up a vector search pipeline?",
        "Where do I search normalized vectors?",
        "What is the simplest way to split a long document?",
    ]:
        print()
        print(f"Query: {query}")
        for rank, result in enumerate(pipeline.search(query, top_k=2), start=1):
            print(f"  {rank}. score={result['score']:.4f} | {result['text']}")


if __name__ == "__main__":
    main()
