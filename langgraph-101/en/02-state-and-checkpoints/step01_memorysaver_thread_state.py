"""Langgraph 101 - Episode 1: Memorysaver thread state."""

from operator import add
from typing import Annotated, cast

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class SessionState(TypedDict):
    """Session state."""

    session_name: str
    turn_count: int
    notes: Annotated[list[str], add]


def remember_visit(state: SessionState):
    """Remember visit."""
    next_turn = state.get("turn_count", 0) + 1
    note = state["notes"][-1]
    print(f"[remember_visit] {state['session_name']} turn {next_turn}: {note}")
    return {"turn_count": next_turn}


def build_graph():
    """Build graph."""
    builder = StateGraph(SessionState)
    builder.add_node("remember_visit", remember_visit)
    builder.add_edge(START, "remember_visit")
    builder.add_edge("remember_visit", END)
    return builder.compile(checkpointer=MemorySaver())


if __name__ == "__main__":
    graph = build_graph()
    config = cast("RunnableConfig", {"configurable": {"thread_id": "en-memory-demo"}})

    first_result = graph.invoke(
        {
            "session_name": "learning session",
            "turn_count": 0,
            "notes": ["saved the first checkpoint"],
        },
        config=config,
    )
    second_result = graph.invoke(
        {
            "session_name": "learning session",
            "turn_count": 0,
            "notes": ["continued with the same thread_id"],
        },
        config=config,
    )

    snapshot = graph.get_state(config)
    history = list(graph.get_state_history(config))

    print("\nFirst result")
    print(first_result)
    print("\nSecond result")
    print(second_result)
    print("\nRestored latest state")
    print(snapshot.values)
    print(f"\nSaved checkpoints: {len(history)}")


# Expected output:
# Thread 1: state saved (checkpoint_id=chk_001)
# Thread 1: state restored successfully
# Messages in thread: 4
