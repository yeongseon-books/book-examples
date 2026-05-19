import os
from typing import Any, cast

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def build_chain():
    parser = JsonOutputParser()
    prompt = ChatPromptTemplate.from_template(
        "Return a study plan for the following topic as JSON only.\n"
        "Use the keys summary, exercises, caution.\n"
        "{format_instructions}\n"
        "Topic: {topic}"
    )
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=cast("Any", os.environ["GROQ_API_KEY"]),
        stop_sequences=None,
    )
    return (
        prompt.partial(format_instructions=parser.get_format_instructions())
        | llm
        | parser
    )


if __name__ == "__main__":
    chain = build_chain()
    result = chain.invoke({"topic": "JsonOutputParser"})
    print("[JsonOutputParser result]")
    print(result)
