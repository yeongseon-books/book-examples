from typing import Literal

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class MultiAgentState(TypedDict):
    question: str
    route: Literal["support", "sales"]
    expert_answer: str


def router_node(state: MultiAgentState):
    sales_keywords = ["price", "cost", "subscription"]
    lowered = state["question"].lower()
    route = (
        "sales" if any(keyword in lowered for keyword in sales_keywords) else "support"
    )
    print(f"[router_node] selected agent: {route}")
    return {"route": route}


def route_selector(state: MultiAgentState) -> str:
    return state["route"]


def support_agent(state: MultiAgentState):
    return {
        "expert_answer": "Support agent: start by checking the checkpointer option in your graph setup."
    }


def sales_agent(state: MultiAgentState):
    return {
        "expert_answer": "Sales agent: the team plan scales its cost with monthly usage."
    }


def build_graph():
    builder = StateGraph(MultiAgentState)
    builder.add_node("router", router_node)
    builder.add_node("support", support_agent)
    builder.add_node("sales", sales_agent)
    builder.add_edge(START, "router")
    builder.add_conditional_edges(
        "router", route_selector, {"support": "support", "sales": "sales"}
    )
    builder.add_edge("support", END)
    builder.add_edge("sales", END)
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    final_state = graph.invoke(
        {"question": "Why does reusing thread_id continue the previous conversation?"}
    )

    print("\nFinal reply")
    print(final_state["expert_answer"])
