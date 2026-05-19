from typing_extensions import TypedDict

from langgraph.graph import END, START, StateGraph


class PipelineState(TypedDict):
    raw_text: str
    cleaned_text: str
    keywords: list[str]
    summary: str


def clean_text(state: PipelineState):
    cleaned_text = " ".join(state["raw_text"].split())
    print(f"[clean_text] 정리된 문장: {cleaned_text}")
    return {"cleaned_text": cleaned_text}


def extract_keywords(state: PipelineState):
    tokens = [token.strip(",.") for token in state["cleaned_text"].split()]
    keywords = tokens[:3]
    print(f"[extract_keywords] 핵심 키워드: {keywords}")
    return {"keywords": keywords}


def summarize_text(state: PipelineState):
    summary = f"이 파이프라인은 {', '.join(state['keywords'])} 중심으로 흐릅니다."
    print(f"[summarize_text] 요약: {summary}")
    return {"summary": summary}


def build_graph():
    builder = StateGraph(PipelineState)
    builder.add_node("clean_text", clean_text)
    builder.add_node("extract_keywords", extract_keywords)
    builder.add_node("summarize_text", summarize_text)
    builder.add_edge(START, "clean_text")
    builder.add_edge("clean_text", "extract_keywords")
    builder.add_edge("extract_keywords", "summarize_text")
    builder.add_edge("summarize_text", END)
    return builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    final_state = graph.invoke(
        {"raw_text": "LangGraph는 상태, 노드, 엣지를 함께 다루는 그래프 오케스트레이터입니다."}
    )

    print("\n최종 상태")
    print(final_state)
