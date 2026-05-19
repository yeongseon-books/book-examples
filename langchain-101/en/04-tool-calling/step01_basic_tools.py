import os
from typing import Any, cast

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq


@tool
def get_course_status(topic: str) -> str:
    """Return the learning progress for a given topic."""
    progress = {
        "lcel": "LCEL study progress is 60% complete.",
        "rag": "RAG study progress is 30% complete.",
    }
    return progress.get(topic.lower(), f"No progress data is available for {topic}.")


if __name__ == "__main__":
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    llm_with_tools = llm.bind_tools([get_course_status])
    response = llm_with_tools.invoke(
        [HumanMessage(content="Tell me the study progress for rag.")]
    )
    print("[Tool call request]")
    print(response)
