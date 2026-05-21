"""Generated from book-content article."""

from langgraph.graph import StateGraph, END
from typing import TypedDict

class AgentState(TypedDict):
    messages: list[dict[str, Any]]
    iterations: int

def call_model(state: AgentState) -> AgentState:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=state["messages"],
        tools=tools_to_openai_format(),
    )
    msg = response.choices[0].message
    state["messages"].append(msg.model_dump())
    state["iterations"] += 1
    return state

def should_continue(state: AgentState) -> str:
    last = state["messages"][-1]
    if not last.get("tool_calls") or state["iterations"] >= 5:
        return END
    return "tools"

graph = StateGraph(AgentState)
graph.add_node("agent", call_model)
graph.add_node("tools", execute_tools_node)
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", should_continue)
graph.add_edge("tools", "agent")
app = graph.compile()
