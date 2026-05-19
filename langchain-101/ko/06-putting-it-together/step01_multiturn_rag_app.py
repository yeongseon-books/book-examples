"""Langchain 101 - Episode 1: Multiturn rag app."""

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
        page_content="LCEL은 LangChain의 구성 요소를 파이프로 연결해 체인을 조립하는 방식입니다."
    ),
    Document(
        page_content="Retriever는 관련 문서를 검색해 RAG 답변의 근거를 제공합니다."
    ),
    Document(
        page_content="Tool calling은 모델이 외부 함수를 호출해 최신 정보나 계산 결과를 가져오게 합니다."
    ),
    Document(
        page_content="Streaming은 첫 토큰을 빨리 보여 주어 대기 시간을 짧게 느끼게 합니다."
    ),
]


def format_docs(docs):
    """Format docs."""
    return "\n\n".join(doc.page_content for doc in docs)


def format_history(chat_history):
    """Format history."""
    if not chat_history:
        return "이전 대화 없음"
    return "\n".join(
        f"사용자: {message.content}"
        if isinstance(message, HumanMessage)
        else f"도우미: {message.content}"
        for message in chat_history
    )


def build_chain():
    """Build chain."""
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(DOCS, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    prompt = ChatPromptTemplate.from_template(
        "당신은 LangChain 학습 도우미입니다.\n"
        "이전 대화:\n{history}\n\n"
        "검색 문맥:\n{context}\n\n"
        "현재 질문: {question}\n"
        "문맥을 우선 사용하고, 부족하면 일반적인 설명을 덧붙여 주세요."
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
    """Main."""
    chain = build_chain()
    chat_history = []
    print("LangChain 멀티턴 RAG 앱입니다. 종료하려면 quit 를 입력하세요.")

    while True:
        question = input("질문> ").strip()
        if not question:
            print("질문을 입력해 주세요.")
            continue
        if question.lower() == "quit":
            print("앱을 종료합니다.")
            break

        answer = chain.invoke({"question": question, "chat_history": chat_history})
        print(f"답변> {answer}")
        chat_history.extend([HumanMessage(content=question), AIMessage(content=answer)])


if __name__ == "__main__":
    main()
