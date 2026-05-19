from typing_extensions import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


class ReviewState(TypedDict):
    review: str
    sentiment: Literal["positive", "negative"]
    action: str
    response: str


def classify_review(state: ReviewState):
    positive_keywords = ["최고", "빠르", "편하", "만족"]
    sentiment = "positive" if any(keyword in state["review"] for keyword in positive_keywords) else "negative"
    print(f"[classify_review] 감정 분류: {sentiment}")
    return {"sentiment": sentiment}


def branch_selector(state: ReviewState) -> str:
    return state["sentiment"]


def handle_positive(state: ReviewState):
    return {"action": "추천 후기로 묶기"}


def handle_negative(state: ReviewState):
    return {"action": "개선 이슈로 전달하기"}


def finalize_response(state: ReviewState):
    response = f"분기 완료: {state['action']} | 원문: {state['review']}"
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
    final_state = graph.invoke({"review": "배송은 조금 늦었지만 사용감은 만족스럽습니다."})

    print("\n최종 상태")
    print(final_state)
