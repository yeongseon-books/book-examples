from operator import add
from typing import Annotated, cast

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class SessionState(TypedDict):
    session_name: str
    turn_count: int
    notes: Annotated[list[str], add]


def remember_visit(state: SessionState):
    next_turn = state.get("turn_count", 0) + 1
    note = state["notes"][-1]
    print(f"[remember_visit] {state['session_name']} 세션 {next_turn}회차 기록: {note}")
    return {"turn_count": next_turn}


def build_graph():
    builder = StateGraph(SessionState)
    builder.add_node("remember_visit", remember_visit)
    builder.add_edge(START, "remember_visit")
    builder.add_edge("remember_visit", END)
    return builder.compile(checkpointer=MemorySaver())


if __name__ == "__main__":
    graph = build_graph()
    config = cast("RunnableConfig", {"configurable": {"thread_id": "ko-memory-demo"}})

    first_result = graph.invoke(
        {
            "session_name": "학습 세션",
            "turn_count": 0,
            "notes": ["첫 번째 체크포인트 저장"],
        },
        config=config,
    )
    second_result = graph.invoke(
        {
            "session_name": "학습 세션",
            "turn_count": 0,
            "notes": ["같은 thread_id로 이어서 실행"],
        },
        config=config,
    )

    snapshot = graph.get_state(config)
    history = list(graph.get_state_history(config))

    print("\n첫 번째 실행 결과")
    print(first_result)
    print("\n두 번째 실행 결과")
    print(second_result)
    print("\n복원된 최신 상태")
    print(snapshot.values)
    print(f"\n저장된 체크포인트 수: {len(history)}")
