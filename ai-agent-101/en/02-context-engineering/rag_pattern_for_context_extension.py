"""Generated from book-content article."""

from typing import List

def retrieve_relevant_docs(query: str, top_k: int = 3) -> List[dict]:
    """
    Finds relevant documents through vector search.
    
    Actual implementation uses:
    - Vector DB (Pinecone, Weaviate, Chroma)
    - Embedding model (OpenAI, Sentence Transformers)
    """
    # Generate query embedding
    query_embedding = get_embedding(query)
    
    # Similarity search
    results = vector_db.search(query_embedding, top_k=top_k)
    
    return [
        {"content": r.text, "score": r.similarity, "source": r.metadata["source"]}
        for r in results
    ]

def build_rag_context(query: str) -> str:
    """Builds context using RAG pattern."""
    docs = retrieve_relevant_docs(query)
    
    context = "Relevant documents:\n\n"
    for i, doc in enumerate(docs, 1):
        context += f"Document {i} (similarity: {doc['score']:.2f}, source: {doc['source']}):\n"
        context += f"{doc['content']}\n\n"
    
    context += f"User query: {query}\n\n"
    context += "Answer based on the above documents. Don't speculate about content not in the documents."
    
    return context
