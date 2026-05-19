"""Langgraph 101 - Episode 1: Toolnode with chatgroq."""

import os
from typing import Annotated

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict


class AgentState(TypedDict):
    """Agent state."""

    messages: Annotated[list, add_messages]


@tool
def get_meeting_room_status(room_name: str) -> str:
    """회의실 예약 상태를 확인합니다."""
    rooms = {
        "오로라": "오후 3시까지 비어 있습니다.",
        "노바": "오후 2시부터 4시까지 예약되어 있습니다.",
    }
    return rooms.get(room_name, f"{room_name} 회의실 정보가 등록되어 있지 않습니다.")


def build_model() -> ChatGroq:
    """Build model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY를 먼저 설정하세요.")
    return ChatGroq(model="llama3-70b-8192", temperature=0, stop_sequences=None)


def assistant_node(state: AgentState):
    """Assistant node."""
    model = build_model().bind_tools([get_meeting_room_status])
    response = model.invoke(
        [
            SystemMessage(
                content="항상 한국어로 답하고, 필요한 경우 도구를 먼저 사용하세요."
            )
        ]
        + state["messages"]
    )
    return {"messages": [response]}


def build_graph():
    """Build graph."""
    builder = StateGraph(AgentState)
    builder.add_node("assistant", assistant_node)
    builder.add_node("tools", ToolNode([get_meeting_room_status]))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant", tools_condition)
    builder.add_edge("tools", "assistant")
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke(
        {"messages": [HumanMessage(content="노바 회의실 지금 쓸 수 있나요?")]}
    )

    print("\n메시지 로그")
    for message in result["messages"]:
        print(f"- {message.type}: {message.content}")
