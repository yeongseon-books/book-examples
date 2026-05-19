import os
from typing import Any, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableMap
from langchain_groq import ChatGroq


def build_chain():
    prompt = ChatPromptTemplate.from_template(
        "주제: {topic}\n난이도: {level}\n위 정보를 바탕으로 학습 계획을 2단계로 작성해 주세요."
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast(Any, os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    parser = StrOutputParser()

    inputs = RunnableMap(
        {
            "topic": RunnableLambda(lambda data: cast(dict[str, Any], data)["topic"]),
            "level": RunnableLambda(
                lambda data: "입문"
                if cast(dict[str, Any], data).get("is_beginner", True)
                else "중급"
            ),
        }
    )
    return inputs | prompt | llm | parser


if __name__ == "__main__":
    chain = build_chain()
    result = chain.invoke({"topic": "RunnableMap", "is_beginner": True})
    print("[RunnableMap 결과]")
    print(result)
