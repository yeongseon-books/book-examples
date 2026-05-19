import os
from typing import Any, cast

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq


@tool
def get_course_status(topic: str) -> str:
    """주어진 주제의 학습 진행 상태를 반환합니다."""
    progress = {
        "lcel": "LCEL 학습은 60% 진행되었습니다.",
        "rag": "RAG 학습은 30% 진행되었습니다.",
    }
    return progress.get(topic.lower(), f"{topic} 주제의 진행 상태 정보가 없습니다.")


if __name__ == "__main__":
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    llm_with_tools = llm.bind_tools([get_course_status])
    response = llm_with_tools.invoke(
        [HumanMessage(content="rag 학습 진행 상태를 알려 주세요.")]
    )
    print("[도구 호출 요청]")
    print(response)
