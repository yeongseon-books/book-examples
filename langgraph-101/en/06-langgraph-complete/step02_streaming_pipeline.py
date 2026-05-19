"""Langgraph 101 - Episode 2: Streaming pipeline."""

import os
from typing import Annotated, cast

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from typing_extensions import TypedDict


class StreamingState(TypedDict):
    """Streaming state."""

    messages: Annotated[list, add_messages]


@tool
def lookup_blog_metric(metric_name: str) -> str:
    """Look up a blog operations metric."""
    metrics = {
        "visitors": "Yesterday's visitors: 1,240.",
        "subscribers": "Current newsletter subscribers: 318.",
    }
    return metrics.get(metric_name.lower(), f"No metric is ready for {metric_name}.")


def build_model() -> ChatGroq:
    """Build model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("Set GROQ_API_KEY before running this example.")
    return ChatGroq(model="llama3-70b-8192", temperature=0, stop_sequences=None)


def assistant_node(state: StreamingState):
    """Assistant node."""
    model = build_model().bind_tools([lookup_blog_metric])
    response = model.invoke(state["messages"])
    return {"messages": [response]}


def should_continue(state: StreamingState):
    """Should continue."""
    last_message = state["messages"][-1]
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    return END


def build_graph():
    """Build graph."""
    builder = StateGraph(StreamingState)
    builder.add_node("assistant", assistant_node)
    builder.add_node("tools", ToolNode([lookup_blog_metric]))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant", should_continue, {"tools": "tools", END: END}
    )
    builder.add_edge("tools", "assistant")
    return builder.compile(checkpointer=MemorySaver())


if __name__ == "__main__":
    graph = build_graph()
    config = cast("RunnableConfig", {"configurable": {"thread_id": "en-stream-demo"}})
    seen = 0

    for event in graph.stream(
        {
            "messages": [
                HumanMessage(
                    content="Tell me the visitors and subscribers metrics in order."
                )
            ]
        },
        config=config,
        stream_mode="values",
    ):
        messages = event["messages"]
        for message in messages[seen:]:
            if isinstance(message, ToolMessage):
                print(f"[tool] {message.content}")
            else:
                print(f"[{message.type}] {message.content}")
        seen = len(messages)

    print("\nStored state after streaming")
    print(graph.get_state(config).values)
