"""Langgraph 101 - Episode 2: Supervisor pattern."""

from operator import add
from typing import Annotated, Literal

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class SupervisorState(TypedDict):
    """Supervisor state."""

    request: str
    remaining_workers: list[str]
    findings: Annotated[list[str], add]
    next_worker: Literal["researcher", "writer", "finish"]
    final_answer: str


def supervisor_node(state: SupervisorState):
    """Supervisor node."""
    next_worker: Literal["researcher", "writer", "finish"]
    if state["remaining_workers"]:
        next_worker = state["remaining_workers"][0]  # type: ignore[assignment]
    else:
        next_worker = "finish"
    print(f"[supervisor_node] next worker: {next_worker}")
    return {"next_worker": next_worker}


def route_selector(state: SupervisorState) -> str:
    """Route selector."""
    return state["next_worker"]


def researcher_agent(state: SupervisorState):
    """Researcher agent."""
    remaining = state["remaining_workers"][1:]
    finding = f"researcher: the key concepts for '{state['request']}' are checkpoints, conditional edges, and tool calls."
    return {"remaining_workers": remaining, "findings": [finding]}


def writer_agent(state: SupervisorState):
    """Writer agent."""
    remaining = state["remaining_workers"][1:]
    finding = "writer: shape the post as problem framing, graph walkthrough, then execution output."
    return {"remaining_workers": remaining, "findings": [finding]}


def finalize_answer(state: SupervisorState):
    """Finalize answer."""
    final_answer = "Supervisor summary\n- " + "\n- ".join(state["findings"])
    return {"final_answer": final_answer}


def build_graph():
    """Build graph."""
    builder = StateGraph(SupervisorState)
    builder.add_node("supervisor", supervisor_node)
    builder.add_node("researcher", researcher_agent)
    builder.add_node("writer", writer_agent)
    builder.add_node("finish", finalize_answer)
    builder.add_edge(START, "supervisor")
    builder.add_conditional_edges(
        "supervisor",
        route_selector,
        {"researcher": "researcher", "writer": "writer", "finish": "finish"},
    )
    builder.add_edge("researcher", "supervisor")
    builder.add_edge("writer", "supervisor")
    builder.add_edge("finish", END)
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    final_state = graph.invoke(
        {
            "request": "Draft the outline for an introductory LangGraph post",
            "remaining_workers": ["researcher", "writer"],
            "findings": [],
        }
    )

    print("\nFinal reply")
    print(final_state["final_answer"])
