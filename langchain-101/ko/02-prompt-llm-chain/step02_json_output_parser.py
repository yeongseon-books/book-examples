import os
from typing import Any, cast

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def build_chain():
    parser = JsonOutputParser()
    prompt = ChatPromptTemplate.from_template(
        "다음 주제에 대한 학습 계획을 JSON으로만 답해 주세요.\n"
        "반드시 keys는 summary, exercises, caution 를 사용하세요.\n"
        "{format_instructions}\n"
        "주제: {topic}"
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast(Any, os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    return prompt.partial(format_instructions=parser.get_format_instructions()) | llm | parser


if __name__ == "__main__":
    chain = build_chain()
    result = chain.invoke({"topic": "JsonOutputParser"})
    print("[JsonOutputParser 결과]")
    print(result)
