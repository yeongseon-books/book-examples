"""Langchain 101 - Episode 2: Async stream."""

import asyncio
import os
from typing import Any, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def build_chain():
    """Build chain."""
    prompt = ChatPromptTemplate.from_template(
        "Explain a LangChain astream example in 2 sentences."
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    parser = StrOutputParser()
    return prompt | llm | parser


async def main():
    """Main."""
    chain = build_chain()
    print("[Asynchronous astream output]")
    async for chunk in chain.astream({}):
        print(chunk, end="", flush=True)
    print()


if __name__ == "__main__":
    asyncio.run(main())
