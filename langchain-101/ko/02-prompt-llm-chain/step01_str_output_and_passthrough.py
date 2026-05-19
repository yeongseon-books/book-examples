import os
from typing import Any, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq


def build_chain():
    prompt = ChatPromptTemplate.from_template(
        "주제: {topic}\n학습 목적: {goal}\n한 문단으로 실전 조언을 작성해 주세요."
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast(Any, os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    parser = StrOutputParser()

    chain = (
        RunnablePassthrough.assign(
            goal=lambda data: data.get("goal", "업무에 바로 적용하기")
        )
        | prompt
        | llm
        | parser
    )
    return chain


if __name__ == "__main__":
    chain = build_chain()
    result = chain.invoke({"topic": "StrOutputParser"})
    print("[StrOutputParser + RunnablePassthrough 결과]")
    print(result)
