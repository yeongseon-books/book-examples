import os
from typing import Any, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def build_chain():
    prompt = ChatPromptTemplate.from_template(
        "다음 주제를 2단계로 설명해 주세요: {topic}"
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast(Any, os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    parser = StrOutputParser()
    return prompt | llm | parser


if __name__ == "__main__":
    chain = build_chain()
    result = chain.invoke({"topic": "LCEL 기본 흐름"})
    print("[기본 체인 결과]")
    print(result)
