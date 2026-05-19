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


# Expected output:
# A list comprehension in Python is a concise way to create lists by
# applying an expression to each item in an iterable, optionally filtering
# items with a condition. The syntax is [expression for item in iterable
# if condition]. For example, [x**2 for x in range(10) if x % 2 == 0]
# produces [0, 4, 16, 36, 64].
