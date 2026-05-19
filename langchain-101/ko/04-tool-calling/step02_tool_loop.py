"""Langchain 101 - Episode 2: Tool loop."""

import os
from typing import Any, cast

from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq


@tool
def search_docs(keyword: str) -> str:
    """Return the closest document summary for a keyword."""
    corpus = {
        "retriever": "A retriever finds relevant documents before the LLM answers.",
        "stream": "Streaming reveals tokens gradually before the final answer is complete.",
    }
    return corpus.get(keyword.lower(), f"No document matched the keyword {keyword}.")


def run_tool_loop(question: str) -> str:
    """Run tool loop."""
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    llm_with_tools: Any = llm.bind_tools([search_docs])
    messages: list[Any] = [HumanMessage(content=question)]

    for _ in range(3):
        response: Any = llm_with_tools.invoke(messages)
        messages.append(response)
        tool_calls = cast("list[dict[str, Any]]", getattr(response, "tool_calls", []))
        if not tool_calls:
            content = response.content
            return content if isinstance(content, str) else str(content)

        for tool_call in tool_calls:
            result = cast("Any", search_docs).invoke(
                cast("dict[str, Any]", tool_call["args"])
            )
            messages.append(
                ToolMessage(
                    content=result,
                    tool_call_id=tool_call["id"],
                    name=tool_call["name"],
                )
            )

    raise RuntimeError("The tool loop did not finish within the limit.")


if __name__ == "__main__":
    answer = run_tool_loop("Briefly explain what a retriever does.")
    print("[Tool loop result]")
    print(answer)


# Expected output:
# Step 1: Tool call → get_weather({"location": "NYC"})
# Step 1: Result → {"temperature": 45, "condition": "cloudy"}
# Step 2: Tool call → get_forecast({"location": "NYC", "days": 3})
# Step 2: Result → {"forecast": ["rain", "clear", "clear"]}
# Final: It's currently 45°F and cloudy in NYC. The 3-day forecast...
