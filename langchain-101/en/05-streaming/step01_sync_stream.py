"""Langchain 101 - Episode 1: Sync stream."""

import os
from typing import Any, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def build_chain():
    """Build chain."""
    prompt = ChatPromptTemplate.from_template(
        "Explain the benefits of LangChain streaming in 3 short bullet points."
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
    print("[Synchronous stream output]")
    for chunk in chain.stream({}):
        print(chunk, end="", flush=True)
    print()
