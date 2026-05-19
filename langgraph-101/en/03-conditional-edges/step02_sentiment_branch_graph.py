from typing_extensions import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


class ReviewState(TypedDict):
    review: str
    sentiment: Literal["positive", "negative"]
    action: str
    response: str


def classify_review(state: ReviewState):
    positive_keywords = ["great", "fast", "easy", "satisfied"]
    lowered = state["review"].lower()
    sentiment = "positive" if any(keyword in lowered for keyword in positive_keywords) else "negative"
    print(f"[classify_review] sentiment: {sentiment}")
    return {"sentiment": sentiment}


def branch_selector(state: ReviewState) -> str:
    return state["sentiment"]


def handle_positive(state: ReviewState):
    return {"action": "group as testimonial"}


def handle_negative(state: ReviewState):
    return {"action": "send to improvement backlog"}


def finalize_response(state: ReviewState):
    response = f"Branch complete: {state['action']} | original review: {state['review']}"
    print(f"[finalize_response] {response}")
    return {"response": response}


def build_graph():
    builder = StateGraph(ReviewState)
    builder.add_node("classify_review", classify_review)
    builder.add_node("handle_positive", handle_positive)
    builder.add_node("handle_negative", handle_negative)
    builder.add_node("finalize_response", finalize_response)
    builder.add_edge(START, "classify_review")
    builder.add_conditional_edges(
        "classify_review",
        branch_selector,
        {"positive": "handle_positive", "negative": "handle_negative"},
    )
    builder.add_edge("handle_positive", "finalize_response")
    builder.add_edge("handle_negative", "finalize_response")
    builder.add_edge("finalize_response", END)
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    final_state = graph.invoke({"review": "Delivery was a bit slow, but the overall experience was easy."})

    print("\nFinal state")
    print(final_state)
