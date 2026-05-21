"""Generated from book-content article."""

from typing import Protocol

class Retriever(Protocol):
    def search(self, query: str, top_k: int) -> list[dict]: ...

class Reranker(Protocol):
    def rerank(self, query: str, docs: list[dict]) -> list[dict]: ...

class Compressor(Protocol):
    def compress(self, query: str, doc: dict) -> str: ...

def build_retrieved_context(
    query: str,
    retriever: Retriever,
    reranker: Reranker,
    compressor: Compressor,
    final_k: int = 5,
) -> list[str]:
    """Three-stage precision pipeline."""
    candidates = retriever.search(query, top_k=30)
    reranked = reranker.rerank(query, candidates)[:final_k]
    compressed = [compressor.compress(query, doc) for doc in reranked]
    return compressed
