"""Langgraph 101 - Episode 1: Router function."""

from typing import Literal

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class RouteState(TypedDict):
    """Route state."""

    text: str
    route: Literal["positive", "negative"]
    result: str


def classify_text(state: RouteState):
    """Classify text."""
    positive_keywords = ["good", "great", "love", "recommend"]
    lowered = state["text"].lower()
    route = (
        "positive"
        if any(keyword in lowered for keyword in positive_keywords)
        else "negative"
    )
    print(f"[classify_text] route: {route}")
    return {"route": route}


def route_selector(state: RouteState) -> str:
    """Route selector."""
    return state["route"]


def positive_path(state: RouteState):
    """Positive path."""
    return {
        "result": f"Moved to the positive path: '{state['text']}' was classified as positive."
    }


def negative_path(state: RouteState):
    """Negative path."""
    return {
        "result": f"Moved to the negative path: '{state['text']}' needs more review."
    }


def build_graph():
    """Build graph."""
    builder = StateGraph(RouteState)
    builder.add_node("classify_text", classify_text)
    builder.add_node("positive", positive_path)
    builder.add_node("negative", negative_path)
    builder.add_edge(START, "classify_text")
    builder.add_conditional_edges(
        "classify_text",
        route_selector,
        {"positive": "positive", "negative": "negative"},
    )
    builder.add_edge("positive", END)
    builder.add_edge("negative", END)
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()

    for sample in [
        "I love how easy this graph example is.",
        "The explanation feels incomplete.",
    ]:
        final_state = graph.invoke({"text": sample})
        print("\nExecution result")
        print(final_state["result"])
