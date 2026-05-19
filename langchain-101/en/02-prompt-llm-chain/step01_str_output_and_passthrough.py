"""Langchain 101 - Episode 1: Str output and passthrough."""

import os
from typing import Any, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq


def build_chain():
    """Build chain."""
    prompt = ChatPromptTemplate.from_template(
        "Topic: {topic}\nLearning goal: {goal}\nWrite one practical paragraph of advice."
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    parser = StrOutputParser()

    chain = (
        RunnablePassthrough.assign(
            goal=lambda data: data.get("goal", "apply it to production work")
        )
        | prompt
        | llm
        | parser
    )
    return chain


if __name__ == "__main__":
    chain = build_chain()
    result = chain.invoke({"topic": "StrOutputParser"})
    print("[StrOutputParser + RunnablePassthrough result]")
    print(result)


# Expected output:
# Step 1: Understand the concept
# Step 2: Apply it to a real problem
# (Parsed as plain string via StrOutputParser)
