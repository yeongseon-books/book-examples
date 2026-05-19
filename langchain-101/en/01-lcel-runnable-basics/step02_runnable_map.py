"""Langchain 101 - Episode 2: Runnable map."""

import os
from typing import Any, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableMap
from langchain_groq import ChatGroq


def build_chain():
    """Build chain."""
    prompt = ChatPromptTemplate.from_template(
        "Topic: {topic}\nLevel: {level}\nCreate a 2-step study plan based on this information."
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    parser = StrOutputParser()

    inputs = RunnableMap(
        {
            "topic": RunnableLambda(lambda data: cast("dict[str, Any]", data)["topic"]),
            "level": RunnableLambda(
                lambda data: "beginner"
                if cast("dict[str, Any]", data).get("is_beginner", True)
                else "intermediate"
            ),
        }
    )
    return inputs | prompt | llm | parser


if __name__ == "__main__":
    chain = build_chain()
    result = chain.invoke({"topic": "RunnableMap", "is_beginner": True})
    print("[RunnableMap result]")
    print(result)


# Expected output:
# {"topic_summary": "LCEL chains are composable...",
#  "fun_fact": "LCEL stands for LangChain Expression Language"}
