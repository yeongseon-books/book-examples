"""Langchain 101 - Episode 1: Build faiss."""

from pathlib import Path

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

DOCS = [
    Document(
        page_content="LCEL connects prompts, models, and parsers like a pipeline."
    ),
    Document(
        page_content="A retriever finds relevant documents first and passes that context to the LLM."
    ),
    Document(
        page_content="Streaming improves perceived latency by showing tokens as they arrive."
    ),
]


def build_vectorstore() -> FAISS:
    """Build vectorstore."""
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_documents(DOCS, embeddings)


if __name__ == "__main__":
    vectorstore = build_vectorstore()
    output_dir = Path(__file__).resolve().parent / "vectorstore"
    output_dir.mkdir(exist_ok=True)
    vectorstore.save_local(str(output_dir))
    print(f"Saved FAISS index to: {output_dir}")
