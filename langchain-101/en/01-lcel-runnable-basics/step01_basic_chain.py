"""Langchain 101 - Episode 1: Basic chain."""

import os
from typing import Any, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def build_chain():
    """Build chain."""
    prompt = ChatPromptTemplate.from_template(
        "Explain the following topic in 2 steps: {topic}"
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
    result = chain.invoke({"topic": "the LCEL pipeline"})
    print("[Basic chain result]")
    print(result)
