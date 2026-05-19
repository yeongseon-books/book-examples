from operator import add
from typing import Annotated, Literal

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class SupervisorState(TypedDict):
    request: str
    remaining_workers: list[str]
    findings: Annotated[list[str], add]
    next_worker: Literal["researcher", "writer", "finish"]
    final_answer: str


def supervisor_node(state: SupervisorState):
    next_worker: Literal["researcher", "writer", "finish"]
    if state["remaining_workers"]:
        next_worker = state["remaining_workers"][0]  # type: ignore[assignment]
    else:
        next_worker = "finish"
    print(f"[supervisor_node] 다음 작업자: {next_worker}")
    return {"next_worker": next_worker}


def route_selector(state: SupervisorState) -> str:
    return state["next_worker"]


def researcher_agent(state: SupervisorState):
    remaining = state["remaining_workers"][1:]
    finding = f"researcher: '{state['request']}'에 필요한 핵심 개념은 체크포인터, 조건부 엣지, 도구 호출입니다."
    return {"remaining_workers": remaining, "findings": [finding]}


def writer_agent(state: SupervisorState):
    remaining = state["remaining_workers"][1:]
    finding = "writer: 도입부는 문제 정의, 본문은 그래프 흐름, 마무리는 실행 결과로 정리합니다."
    return {"remaining_workers": remaining, "findings": [finding]}


def finalize_answer(state: SupervisorState):
    final_answer = "감독자 요약\n- " + "\n- ".join(state["findings"])
    return {"final_answer": final_answer}


def build_graph():
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
            "request": "LangGraph 입문 글의 구성안을 잡아줘",
            "remaining_workers": ["researcher", "writer"],
            "findings": [],
        }
    )

    print("\n최종 응답")
    print(final_state["final_answer"])
