import os
from typing import Annotated

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from typing_extensions import TypedDict


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


@tool
def search_team_calendar(team_name: str) -> str:
    """팀 일정표에서 이번 주 핵심 일정을 찾습니다."""
    calendar = {
        "플랫폼": "수요일 배포 리허설, 금요일 장애 대응 훈련",
        "데이터": "화요일 지표 리뷰, 목요일 파이프라인 점검",
    }
    return calendar.get(team_name, f"{team_name} 팀 일정은 아직 등록되지 않았습니다.")


@tool
def lookup_lunch_menu(day: str) -> str:
    """사내 식당 점심 메뉴를 조회합니다."""
    menus = {
        "수요일": "비빔밥과 된장국",
        "목요일": "불고기 덮밥과 샐러드",
    }
    return menus.get(day, f"{day} 메뉴 정보가 없습니다.")


def build_model() -> ChatGroq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY를 먼저 설정하세요.")
    return ChatGroq(model="llama3-70b-8192", temperature=0, stop_sequences=None)


def assistant_node(state: AgentState):
    tools = [search_team_calendar, lookup_lunch_menu]
    model = build_model().bind_tools(tools)
    response = model.invoke(
        [
            SystemMessage(
                content="일정과 식단 질문에 답할 때 필요한 도구를 먼저 사용하고, 마지막 답변은 한국어로 정리하세요."
            )
        ]
        + state["messages"]
    )
    return {"messages": [response]}


def should_continue(state: AgentState):
    last_message = state["messages"][-1]
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    return END


def build_graph():
    tools = [search_team_calendar, lookup_lunch_menu]
    builder = StateGraph(AgentState)
    builder.add_node("assistant", assistant_node)
    builder.add_node("tools", ToolNode(tools))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant", should_continue, {"tools": "tools", END: END}
    )
    builder.add_edge("tools", "assistant")
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content="플랫폼 팀 이번 주 일정과 수요일 점심 메뉴를 알려주세요."
                )
            ]
        }
    )

    print("\n에이전트 루프 결과")
    for message in result["messages"]:
        print(f"- {message.type}: {message.content}")
