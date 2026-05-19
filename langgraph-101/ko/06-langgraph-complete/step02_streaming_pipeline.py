import os
from typing import Annotated, cast

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from typing_extensions import TypedDict


class StreamingState(TypedDict):
    messages: Annotated[list, add_messages]


@tool
def lookup_blog_metric(metric_name: str) -> str:
    """블로그 운영 지표를 조회합니다."""
    metrics = {
        "방문자": "어제 방문자는 1,240명입니다.",
        "구독자": "현재 뉴스레터 구독자는 318명입니다.",
    }
    return metrics.get(metric_name, f"{metric_name} 지표는 준비되지 않았습니다.")


def build_model() -> ChatGroq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY를 먼저 설정하세요.")
    return ChatGroq(model="llama3-70b-8192", temperature=0, stop_sequences=None)


def assistant_node(state: StreamingState):
    model = build_model().bind_tools([lookup_blog_metric])
    response = model.invoke(state["messages"])
    return {"messages": [response]}


def should_continue(state: StreamingState):
    last_message = state["messages"][-1]
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    return END


def build_graph():
    builder = StateGraph(StreamingState)
    builder.add_node("assistant", assistant_node)
    builder.add_node("tools", ToolNode([lookup_blog_metric]))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant", should_continue, {"tools": "tools", END: END}
    )
    builder.add_edge("tools", "assistant")
    return builder.compile(checkpointer=MemorySaver())


if __name__ == "__main__":
    graph = build_graph()
    config = cast("RunnableConfig", {"configurable": {"thread_id": "ko-stream-demo"}})
    seen = 0

    for event in graph.stream(
        {
            "messages": [
                HumanMessage(content="방문자와 구독자 지표를 차례대로 알려주세요.")
            ]
        },
        config=config,
        stream_mode="values",
    ):
        messages = event["messages"]
        for message in messages[seen:]:
            if isinstance(message, ToolMessage):
                print(f"[tool] {message.content}")
            else:
                print(f"[{message.type}] {message.content}")
        seen = len(messages)

    print("\n스트리밍 후 저장된 상태")
    print(graph.get_state(config).values)
