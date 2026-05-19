from __future__ import annotations

from common.models import (
    BenchmarkConfig,
    EmbeddingCandidate,
    GenerationCase,
    PipelineCase,
    QueryGroundTruth,
    VectorIndexCandidate,
)

CORPUS = [
    {
        "id": "d01",
        "text": "A vector database stores embedding vectors and supports similarity search.",
        "topic": "vectordb",
    },
    {
        "id": "d02",
        "text": "FAISS is a high-performance vector search library created by Facebook AI Research.",
        "topic": "faiss",
    },
    {
        "id": "d03",
        "text": "IndexFlatIP provides exact inner-product search.",
        "topic": "faiss",
    },
    {
        "id": "d04",
        "text": "Cosine similarity measures directional similarity between vectors.",
        "topic": "similarity",
    },
    {
        "id": "d05",
        "text": "HNSW is a graph-based ANN index designed for fast approximate search.",
        "topic": "ann",
    },
    {
        "id": "d06",
        "text": "Embedding models convert text into numeric vectors placed in semantic space.",
        "topic": "embedding",
    },
    {
        "id": "d07",
        "text": "all-MiniLM-L6-v2 is a light 384-dimensional embedding model.",
        "topic": "embedding",
    },
    {
        "id": "d08",
        "text": "Very small chunks lose context, while very large chunks add noise.",
        "topic": "chunking",
    },
    {
        "id": "d09",
        "text": "Hybrid search combines keyword and vector retrieval to improve recall.",
        "topic": "hybrid",
    },
    {
        "id": "d10",
        "text": "Re-ranking reorders first-pass retrieval results to improve precision.",
        "topic": "reranking",
    },
]

QUERIES = [
    QueryGroundTruth("What is FAISS?", {"d02", "d03"}, "faiss"),
    QueryGroundTruth("How do embedding models work?", {"d06", "d07"}, "embedding"),
    QueryGroundTruth(
        "How are cosine similarity and inner product related?",
        {"d03", "d04"},
        "similarity",
    ),
    QueryGroundTruth("What kind of index is HNSW?", {"d05"}, "ann"),
    QueryGroundTruth(
        "How does chunk size affect retrieval quality?", {"d08"}, "chunking"
    ),
    QueryGroundTruth("Why use hybrid search?", {"d09"}, "hybrid"),
]

GENERATION_CASE = GenerationCase(
    question="What kind of tool is FAISS?",
    context="FAISS is a high-performance vector search library created by Facebook AI Research. IndexFlatIP provides exact inner-product search.",
    answer="FAISS is a library for fast large-scale vector retrieval, and it also supports exact search through indexes such as IndexFlatIP.",
)

PIPELINE_CASES = [
    PipelineCase(
        "What is FAISS?",
        {"d02", "d03"},
        "FAISS is a high-performance vector search library.",
    ),
    PipelineCase(
        "How do embedding models work?",
        {"d06", "d07"},
        "Embedding models convert text into semantic vectors.",
    ),
    PipelineCase(
        "Why use hybrid search?",
        {"d09"},
        "Hybrid search combines keyword and vector retrieval for better coverage.",
    ),
]

EMBEDDING_MODELS = [
    EmbeddingCandidate("minilm", "sentence-transformers/all-MiniLM-L6-v2"),
    EmbeddingCandidate("mpnet", "sentence-transformers/all-mpnet-base-v2"),
]

VECTOR_INDEXES = [
    VectorIndexCandidate("flat", "Flat"),
    VectorIndexCandidate("hnsw32", "HNSW32"),
    VectorIndexCandidate("ivf32_flat", "IVF32,Flat"),
]

FULL_CONFIGS = [
    BenchmarkConfig(
        name="baseline-en",
        embedding_model="sentence-transformers/all-MiniLM-L6-v2",
        top_k=3,
        answer_prompt="Answer the question using only the context below. If the answer is missing, say so clearly.\n\nContext:\n{context}\n\nQuestion:\n{question}",
    ),
    BenchmarkConfig(
        name="mpnet-en",
        embedding_model="sentence-transformers/all-mpnet-base-v2",
        top_k=3,
        answer_prompt="Answer the question using only the context below. If the answer is missing, say so clearly.\n\nContext:\n{context}\n\nQuestion:\n{question}",
    ),
]
