from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class GraphState(TypedDict):
    user_input: str
    normalized_input: str
    reply: str


def normalize_input(state: GraphState):
    normalized = state["user_input"].strip()
    print(f"[normalize_input] 정리된 입력: {normalized}")
    return {"normalized_input": normalized}


def create_reply(state: GraphState):
    reply = (
        f"안녕하세요. '{state['normalized_input']}' 주제로 LangGraph를 시작해봅시다."
    )
    print(f"[create_reply] 생성된 답변: {reply}")
    return {"reply": reply}


def build_graph():
    builder = StateGraph(GraphState)
    builder.add_node("normalize_input", normalize_input)
    builder.add_node("create_reply", create_reply)
    builder.add_edge(START, "normalize_input")
    builder.add_edge("normalize_input", "create_reply")
    builder.add_edge("create_reply", END)
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    final_state = graph.invoke({"user_input": "  LangGraph 입문 예제  "})

    print("\n최종 상태")
    print(final_state)
