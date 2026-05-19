from typing_extensions import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


class RouteState(TypedDict):
    text: str
    route: Literal["positive", "negative"]
    result: str


def classify_text(state: RouteState):
    positive_keywords = ["좋", "만족", "추천"]
    route = "positive" if any(keyword in state["text"] for keyword in positive_keywords) else "negative"
    print(f"[classify_text] 라우팅 결과: {route}")
    return {"route": route}


def route_selector(state: RouteState) -> str:
    return state["route"]


def positive_path(state: RouteState):
    return {"result": f"긍정 흐름으로 이동: '{state['text']}'는 좋은 반응으로 분류되었습니다."}


def negative_path(state: RouteState):
    return {"result": f"부정 흐름으로 이동: '{state['text']}'는 추가 확인이 필요합니다."}


def build_graph():
    builder = StateGraph(RouteState)
    builder.add_node("classify_text", classify_text)
    builder.add_node("positive", positive_path)
    builder.add_node("negative", negative_path)
    builder.add_edge(START, "classify_text")
    builder.add_conditional_edges("classify_text", route_selector, {"positive": "positive", "negative": "negative"})
    builder.add_edge("positive", END)
    builder.add_edge("negative", END)
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()

    for sample in ["이 예제는 이해가 잘 돼서 만족스럽습니다.", "설명이 모호해서 조금 아쉽습니다."]:
        final_state = graph.invoke({"text": sample})
        print("\n실행 결과")
        print(final_state["result"])
