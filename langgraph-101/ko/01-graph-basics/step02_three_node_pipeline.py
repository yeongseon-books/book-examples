"""Langgraph 101 - Episode 2: Three node pipeline."""

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class PipelineState(TypedDict):
    """Pipeline state."""

    raw_text: str
    cleaned_text: str
    keywords: list[str]
    summary: str


def clean_text(state: PipelineState):
    """Clean text."""
    cleaned_text = " ".join(state["raw_text"].split())
    print(f"[clean_text] cleaned sentence: {cleaned_text}")
    return {"cleaned_text": cleaned_text}


def extract_keywords(state: PipelineState):
    """Extract keywords."""
    tokens = [token.strip(",.") for token in state["cleaned_text"].split()]
    keywords = tokens[:3]
    print(f"[extract_keywords] keywords: {keywords}")
    return {"keywords": keywords}


def summarize_text(state: PipelineState):
    """Summarize text."""
    summary = f"This pipeline flows around {', '.join(state['keywords'])}."
    print(f"[summarize_text] summary: {summary}")
    return {"summary": summary}


def build_graph():
    """Build graph."""
    builder = StateGraph(PipelineState)
    builder.add_node("clean_text", clean_text)
    builder.add_node("extract_keywords", extract_keywords)
    builder.add_node("summarize_text", summarize_text)
    builder.add_edge(START, "clean_text")
    builder.add_edge("clean_text", "extract_keywords")
    builder.add_edge("extract_keywords", "summarize_text")
    builder.add_edge("summarize_text", END)
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    final_state = graph.invoke(
        {
            "raw_text": "LangGraph orchestrates state, nodes, and edges in one graph runtime."
        }
    )

    print("\nFinal state")
    print(final_state)


# Expected output:
# Node 'start' executed
# Node 'end' executed
# Final state: {'message': 'processed'}
