"""Langgraph 101 - Episode 1: Checkpoint router tools."""

import os
from typing import Annotated, cast

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from typing_extensions import TypedDict


class WorkflowState(TypedDict):
    """Workflow state."""

    messages: Annotated[list, add_messages]


@tool
def get_order_status(order_id: str) -> str:
    """주문 번호의 현재 배송 상태를 조회합니다."""
    orders = {
        "1001": "상품 준비 중이며 내일 오전 출고 예정입니다.",
        "1002": "오늘 배송 완료되었습니다.",
    }
    return orders.get(order_id, f"주문 번호 {order_id} 정보가 없습니다.")


@tool
def get_shipping_eta(order_id: str) -> str:
    """주문 번호의 예상 도착 일정을 조회합니다."""
    eta = {
        "1001": "모레 오후 도착 예정입니다.",
        "1002": "이미 배송이 완료된 주문입니다.",
    }
    return eta.get(order_id, f"주문 번호 {order_id}의 도착 예정일을 찾지 못했습니다.")


def build_model() -> ChatGroq:
    """Build model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY를 먼저 설정하세요.")
    return ChatGroq(model="llama3-70b-8192", temperature=0, stop_sequences=None)


def assistant_node(state: WorkflowState):
    """Assistant node."""
    tools = [get_order_status, get_shipping_eta]
    model = build_model().bind_tools(tools)
    response = model.invoke(
        [
            SystemMessage(
                content="항상 한국어로 답하고, 주문 조회가 필요하면 먼저 적절한 도구를 사용하세요."
            )
        ]
        + state["messages"]
    )
    return {"messages": [response]}


def should_continue(state: WorkflowState):
    """Should continue."""
    last_message = state["messages"][-1]
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    return END


def build_graph():
    """Build graph."""
    tools = [get_order_status, get_shipping_eta]
    builder = StateGraph(WorkflowState)
    builder.add_node("assistant", assistant_node)
    builder.add_node("tools", ToolNode(tools))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant", should_continue, {"tools": "tools", END: END}
    )
    builder.add_edge("tools", "assistant")
    return builder.compile(checkpointer=MemorySaver())


if __name__ == "__main__":
    graph = build_graph()
    config = cast("RunnableConfig", {"configurable": {"thread_id": "ko-complete-demo"}})

    graph.invoke(
        {"messages": [HumanMessage(content="주문번호 1001 상태를 알려주세요.")]},
        config=config,
    )
    second_result = graph.invoke(
        {
            "messages": [
                HumanMessage(content="그 주문의 도착 예정일도 이어서 알려주세요.")
            ]
        },
        config=config,
    )

    print("\n최종 메시지 로그")
    for message in second_result["messages"]:
        print(f"- {message.type}: {message.content}")

    print("\n체크포인트에 저장된 현재 상태")
    print(graph.get_state(config).values)
