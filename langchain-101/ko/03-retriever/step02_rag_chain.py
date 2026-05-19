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
    Document(page_content="LangChain Retriever는 질문과 관련된 문서를 검색해 LLM 입력에 포함합니다."),
    Document(page_content="FAISS는 벡터 유사도 검색에 자주 사용하는 경량 벡터 저장소입니다."),
    Document(page_content="RAG는 검색 결과를 바탕으로 더 근거 있는 답변을 생성하는 패턴입니다."),
]


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def build_chain():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(DOCS, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    prompt = ChatPromptTemplate.from_template(
        "당신은 LangChain 튜터입니다.\n"
        "문맥:\n{context}\n\n"
        "질문: {question}\n"
        "문맥에 근거해 간결하게 답해 주세요."
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast(Any, os.environ["GROQ_API_KEY"]),
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
    result = chain.invoke({"question": "RAG에서 Retriever는 왜 필요한가요?"})
    print("[RAG 체인 결과]")
    print(result)
