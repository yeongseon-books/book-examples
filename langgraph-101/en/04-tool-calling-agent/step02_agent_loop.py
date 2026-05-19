"""Langgraph 101 - Episode 2: Agent loop."""

import os
from typing import Annotated

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from typing_extensions import TypedDict


class AgentState(TypedDict):
    """Agent state."""

    messages: Annotated[list, add_messages]


@tool
def search_team_calendar(team_name: str) -> str:
    """Look up the most important events for a team this week."""
    calendar = {
        "platform": "Wednesday deployment rehearsal, Friday incident drill",
        "data": "Tuesday metrics review, Thursday pipeline check",
    }
    return calendar.get(
        team_name.lower(), f"No schedule is registered for the {team_name} team."
    )


@tool
def lookup_lunch_menu(day: str) -> str:
    """Look up the cafeteria lunch menu."""
    menus = {
        "wednesday": "Bibimbap and soybean paste soup",
        "thursday": "Bulgogi rice bowl and salad",
    }
    return menus.get(day.lower(), f"No lunch menu is available for {day}.")


def build_model() -> ChatGroq:
    """Build model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("Set GROQ_API_KEY before running this example.")
    return ChatGroq(model="llama3-70b-8192", temperature=0, stop_sequences=None)


def assistant_node(state: AgentState):
    """Assistant node."""
    tools = [search_team_calendar, lookup_lunch_menu]
    model = build_model().bind_tools(tools)
    response = model.invoke(
        [
            SystemMessage(
                content="Use tools before answering schedule or menu questions, then summarize in English."
            )
        ]
        + state["messages"]
    )
    return {"messages": [response]}


def should_continue(state: AgentState):
    """Should continue."""
    last_message = state["messages"][-1]
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    return END


def build_graph():
    """Build graph."""
    tools = [search_team_calendar, lookup_lunch_menu]
    builder = StateGraph(AgentState)
    builder.add_node("assistant", assistant_node)
    builder.add_node("tools", ToolNode(tools))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant", should_continue, {"tools": "tools", END: END}
    )
    builder.add_edge("tools", "assistant")
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Tell me the platform team schedule and the Wednesday lunch menu."
                )
            ]
        }
    )

    print("\nAgent loop result")
    for message in result["messages"]:
        print(f"- {message.type}: {message.content}")


# Expected output:
# Agent: I need to check the weather.
# Tool call: get_weather(location="Tokyo")
# Tool result: 72°F, sunny
# Agent: The weather in Tokyo is 72°F and sunny.
