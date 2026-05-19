import os
from typing import Any, cast

from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq


@tool
def search_docs(keyword: str) -> str:
    """키워드와 가장 가까운 문서 요약을 반환합니다."""
    corpus = {
        "retriever": "Retriever는 질문과 관련된 문서를 먼저 찾은 뒤 LLM에 전달합니다.",
        "stream": "Streaming은 응답이 완성되기 전에 토큰을 순차적으로 보여 줍니다.",
    }
    return corpus.get(
        keyword.lower(), f"{keyword} 키워드에 대한 문서를 찾지 못했습니다."
    )


def run_tool_loop(question: str) -> str:
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    llm_with_tools: Any = llm.bind_tools([search_docs])
    messages: list[Any] = [HumanMessage(content=question)]

    for _ in range(3):
        response: Any = llm_with_tools.invoke(messages)
        messages.append(response)
        tool_calls = cast("list[dict[str, Any]]", getattr(response, "tool_calls", []))
        if not tool_calls:
            content = response.content
            return content if isinstance(content, str) else str(content)

        for tool_call in tool_calls:
            result = cast("Any", search_docs).invoke(
                cast("dict[str, Any]", tool_call["args"])
            )
            messages.append(
                ToolMessage(
                    content=result,
                    tool_call_id=tool_call["id"],
                    name=tool_call["name"],
                )
            )

    raise RuntimeError("도구 호출 루프가 제한 횟수 안에 끝나지 않았습니다.")


if __name__ == "__main__":
    answer = run_tool_loop("retriever가 하는 일을 간단히 설명해 주세요.")
    print("[도구 루프 결과]")
    print(answer)
