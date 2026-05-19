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
        if "my name is" in text.lower():
            return text.split("is", 1)[1].strip(" .")
    return None


def assistant_node(state: ChatState):
    last_message = state["messages"][-1]
    remembered_name = find_name(state["messages"][:-1]) or find_name(state["messages"])

    if "my name is" in last_message.content.lower():
        reply = "Got it. I will remember your name for the next turn."
    elif "my name" in last_message.content.lower() and remembered_name:
        reply = f"Of course. The name I remember is {remembered_name}."
    else:
        reply = "This conversation continues as long as you reuse the same thread_id."

    print(f"[assistant_node] reply: {reply}")
    return {"messages": [AIMessage(content=reply)]}


def build_graph():
    builder = StateGraph(ChatState)
    builder.add_node("assistant", assistant_node)
    builder.add_edge(START, "assistant")
    builder.add_edge("assistant", END)
    return builder.compile(checkpointer=MemorySaver())


if __name__ == "__main__":
    graph = build_graph()
    config = cast("RunnableConfig", {"configurable": {"thread_id": "en-chat-thread"}})

    graph.invoke(
        {"messages": [HumanMessage(content="My name is Mina.")]}, config=config
    )
    graph.invoke(
        {"messages": [HumanMessage(content="What was my name again?")]}, config=config
    )

    snapshot = graph.get_state(config)

    print("\nAccumulated conversation state")
    for message in snapshot.values["messages"]:
        print(f"- {message.type}: {message.content}")
