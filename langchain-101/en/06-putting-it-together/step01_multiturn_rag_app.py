import os
from typing import Any, cast

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

DOCS = [
    Document(
        page_content="LCEL assembles LangChain building blocks by piping them together."
    ),
    Document(
        page_content="A retriever searches for relevant documents and provides evidence for RAG answers."
    ),
    Document(
        page_content="Tool calling lets a model use external functions for fresh data or calculations."
    ),
    Document(
        page_content="Streaming improves perceived latency by showing the first tokens early."
    ),
]


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def format_history(chat_history):
    if not chat_history:
        return "No prior conversation"
    return "\n".join(
        f"User: {message.content}"
        if isinstance(message, HumanMessage)
        else f"Assistant: {message.content}"
        for message in chat_history
    )


def build_chain():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(DOCS, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    prompt = ChatPromptTemplate.from_template(
        "You are a LangChain learning assistant.\n"
        "Conversation so far:\n{history}\n\n"
        "Retrieved context:\n{context}\n\n"
        "Current question: {question}\n"
        "Use the context first, then add a short general explanation if needed."
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    parser = StrOutputParser()

    return (
        RunnablePassthrough.assign(
            context=lambda data: format_docs(retriever.invoke(data["question"])),
            history=lambda data: format_history(data["chat_history"]),
        )
        | prompt
        | llm
        | parser
    )


def main():
    chain = build_chain()
    chat_history = []
    print("LangChain multi-turn RAG app. Type quit to exit.")

    while True:
        question = input("Question> ").strip()
        if not question:
            print("Please enter a question.")
            continue
        if question.lower() == "quit":
            print("Closing the app.")
            break

        answer = chain.invoke({"question": question, "chat_history": chat_history})
        print(f"Answer> {answer}")
        chat_history.extend([HumanMessage(content=question), AIMessage(content=answer)])


if __name__ == "__main__":
    main()
