"""Langgraph 101 - Episode 1: Toolnode with chatgroq."""

import os
from typing import Annotated

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict


class AgentState(TypedDict):
    """Agent state."""

    messages: Annotated[list, add_messages]


@tool
def get_meeting_room_status(room_name: str) -> str:
    """Check the reservation status of a meeting room."""
    rooms = {
        "aurora": "It is free until 3 PM.",
        "nova": "It is reserved from 2 PM to 4 PM.",
    }
    return rooms.get(
        room_name.lower(), f"There is no registered information for {room_name}."
    )


def build_model() -> ChatGroq:
    """Build model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("Set GROQ_API_KEY before running this example.")
    return ChatGroq(model="llama3-70b-8192", temperature=0, stop_sequences=None)


def assistant_node(state: AgentState):
    """Assistant node."""
    model = build_model().bind_tools([get_meeting_room_status])
    response = model.invoke(
        [
            SystemMessage(
                content="Always answer in English and use a tool first when it helps."
            )
        ]
        + state["messages"]
    )
    return {"messages": [response]}


def build_graph():
    """Build graph."""
    builder = StateGraph(AgentState)
    builder.add_node("assistant", assistant_node)
    builder.add_node("tools", ToolNode([get_meeting_room_status]))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant", tools_condition)
    builder.add_edge("tools", "assistant")
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke(
        {"messages": [HumanMessage(content="Can I use the nova room right now?")]}
    )

    print("\nMessage log")
    for message in result["messages"]:
        print(f"- {message.type}: {message.content}")
