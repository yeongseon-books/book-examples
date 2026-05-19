"""Langchain 101 - Episode 1: Build faiss."""

from pathlib import Path

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

DOCS = [
    Document(
        page_content="LCEL은 prompt, model, parser를 파이프처럼 연결하는 방식입니다."
    ),
    Document(
        page_content="Retriever는 질문과 관련된 문서를 먼저 찾고, 그 문맥을 LLM에 전달합니다."
    ),
    Document(
        page_content="Streaming은 긴 응답을 토큰 단위로 보여 주어 체감 속도를 높입니다."
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
    print(f"FAISS 인덱스를 저장했습니다: {output_dir}")
