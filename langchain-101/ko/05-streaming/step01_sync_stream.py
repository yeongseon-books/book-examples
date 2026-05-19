import os
from typing import Any, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def build_chain():
    prompt = ChatPromptTemplate.from_template(
        "LangChain streaming의 장점을 짧은 bullet 3개로 설명해 주세요."
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    parser = StrOutputParser()
    return prompt | llm | parser


if __name__ == "__main__":
    chain = build_chain()
    print("[동기 stream 출력]")
    for chunk in chain.stream({}):
        print(chunk, end="", flush=True)
    print()
