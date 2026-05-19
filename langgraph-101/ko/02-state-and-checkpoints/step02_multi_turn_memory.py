from typing import Annotated, cast

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]


def find_name(messages: list) -> str | None:
    for message in reversed(messages):
        if not isinstance(message, HumanMessage):
            continue
        text = message.content if isinstance(message.content, str) else ""
        if "제 이름은" in text:
            return text.split("제 이름은", 1)[1].replace("입니다", "").strip(" .")
    return None


def assistant_node(state: ChatState):
    last_message = state["messages"][-1]
    remembered_name = find_name(state["messages"][:-1]) or find_name(state["messages"])

    if "제 이름은" in last_message.content:
        reply = "이름을 기억해 둘게요. 다음 질문에서 다시 활용해보겠습니다."
    elif "내 이름" in last_message.content and remembered_name:
        reply = f"물론이죠. 지금까지 기억한 이름은 {remembered_name}입니다."
    else:
        reply = "이 대화는 같은 thread_id 안에서 계속 이어집니다."

    print(f"[assistant_node] 응답: {reply}")
    return {"messages": [AIMessage(content=reply)]}


def build_graph():
    builder = StateGraph(ChatState)
    builder.add_node("assistant", assistant_node)
    builder.add_edge(START, "assistant")
    builder.add_edge("assistant", END)
    return builder.compile(checkpointer=MemorySaver())


if __name__ == "__main__":
    graph = build_graph()
    config = cast(RunnableConfig, {"configurable": {"thread_id": "ko-chat-thread"}})

    graph.invoke({"messages": [HumanMessage(content="제 이름은 민준입니다.")]}, config=config)
    graph.invoke({"messages": [HumanMessage(content="방금 말한 내 이름이 뭐였죠?")]}, config=config)

    snapshot = graph.get_state(config)

    print("\n누적 대화 상태")
    for message in snapshot.values["messages"]:
        print(f"- {message.type}: {message.content}")
