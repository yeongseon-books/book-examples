"""Langgraph 101 - Episode 1: Dual agent routing."""

from typing import Literal

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class MultiAgentState(TypedDict):
    """Multi agent state."""

    question: str
    route: Literal["support", "sales"]
    expert_answer: str


def router_node(state: MultiAgentState):
    """Router node."""
    sales_keywords = ["가격", "요금", "구독"]
    route = (
        "sales"
        if any(keyword in state["question"] for keyword in sales_keywords)
        else "support"
    )
    print(f"[router_node] 선택된 에이전트: {route}")
    return {"route": route}


def route_selector(state: MultiAgentState) -> str:
    """Route selector."""
    return state["route"]


def support_agent(state: MultiAgentState):
    """Support agent."""
    return {
        "expert_answer": "지원 에이전트: 설정 화면의 체크포인터 옵션부터 확인해보세요."
    }


def sales_agent(state: MultiAgentState):
    """Sales agent."""
    return {
        "expert_answer": "세일즈 에이전트: 팀 플랜은 월간 사용량 기준으로 비용이 늘어납니다."
    }


def build_graph():
    """Build graph."""
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
        {"question": "체크포인터를 켜면 이전 대화가 왜 이어지나요?"}
    )

    print("\n최종 응답")
    print(final_state["expert_answer"])
