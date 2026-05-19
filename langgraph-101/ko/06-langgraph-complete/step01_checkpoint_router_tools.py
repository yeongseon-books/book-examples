"""Langgraph 101 - Episode 1: Checkpoint router tools."""

import os
from typing import Annotated, cast

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from typing_extensions import TypedDict


class WorkflowState(TypedDict):
    """Workflow state."""

    messages: Annotated[list, add_messages]


@tool
def get_order_status(order_id: str) -> str:
    """Look up the current delivery status for an order number."""
    orders = {
        "1001": "The package is being prepared and will ship tomorrow morning.",
        "1002": "The package was delivered today.",
    }
    return orders.get(order_id, f"There is no information for order {order_id}.")


@tool
def get_shipping_eta(order_id: str) -> str:
    """Look up the expected arrival time for an order number."""
    eta = {
        "1001": "It is expected to arrive tomorrow afternoon.",
        "1002": "This order has already been delivered.",
    }
    return eta.get(order_id, f"Could not find an ETA for order {order_id}.")


def build_model() -> ChatGroq:
    """Build model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("Set GROQ_API_KEY before running this example.")
    return ChatGroq(model="llama3-70b-8192", temperature=0, stop_sequences=None)


def assistant_node(state: WorkflowState):
    """Assistant node."""
    tools = [get_order_status, get_shipping_eta]
    model = build_model().bind_tools(tools)
    response = model.invoke(
        [
            SystemMessage(
                content="Always answer in English and use the right tool before replying about an order."
            )
        ]
        + state["messages"]
    )
    return {"messages": [response]}


def should_continue(state: WorkflowState):
    """Should continue."""
    last_message = state["messages"][-1]
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    return END


def build_graph():
    """Build graph."""
    tools = [get_order_status, get_shipping_eta]
    builder = StateGraph(WorkflowState)
    builder.add_node("assistant", assistant_node)
    builder.add_node("tools", ToolNode(tools))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant", should_continue, {"tools": "tools", END: END}
    )
    builder.add_edge("tools", "assistant")
    return builder.compile(checkpointer=MemorySaver())


if __name__ == "__main__":
    graph = build_graph()
    config = cast("RunnableConfig", {"configurable": {"thread_id": "en-complete-demo"}})

    graph.invoke(
        {"messages": [HumanMessage(content="Please check the status of order 1001.")]},
        config=config,
    )
    second_result = graph.invoke(
        {
            "messages": [
                HumanMessage(content="Now tell me the ETA for that same order.")
            ]
        },
        config=config,
    )

    print("\nFinal message log")
    for message in second_result["messages"]:
        print(f"- {message.type}: {message.content}")

    print("\nCurrent state stored in the checkpoint")
    print(graph.get_state(config).values)


# Expected output:
# Input: 'Write a poem about coding'
# Router → creative_agent
# Response: In lines of code, we find our art...
