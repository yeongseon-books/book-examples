import os
from typing import Any, cast

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

DOCS = [
    Document(
        page_content="A LangChain retriever searches for documents related to the question and injects them into the prompt."
    ),
    Document(
        page_content="FAISS is a lightweight vector store commonly used for similarity search."
    ),
    Document(
        page_content="RAG generates more grounded answers by using retrieved context."
    ),
]


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def build_chain():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(DOCS, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    prompt = ChatPromptTemplate.from_template(
        "You are a LangChain tutor.\n"
        "Context:\n{context}\n\n"
        "Question: {question}\n"
        "Answer briefly and stay grounded in the context."
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    parser = StrOutputParser()

    return (
        RunnablePassthrough.assign(
            context=lambda data: format_docs(retriever.invoke(data["question"]))
        )
        | prompt
        | llm
        | parser
    )


if __name__ == "__main__":
    chain = build_chain()
    result = chain.invoke({"question": "Why does RAG need a retriever?"})
    print("[RAG chain result]")
    print(result)
