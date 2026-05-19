import json
import os
from typing import Any, cast

from groq import Groq


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "도시의 현재 날씨를 반환합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "도시 이름"},
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "온도 단위",
                    },
                },
                "required": ["city"],
            },
        },
    }
]


def get_weather(city: str, unit: str = "celsius") -> dict:
    return {"city": city, "temperature": 22, "unit": unit, "condition": "맑음"}


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "서울 날씨를 알려주세요."}],
        tools=cast(Any, TOOLS),
        tool_choice="auto",
    )

    choice = response.choices[0]
    print(f"finish_reason: {choice.finish_reason}")

    if choice.finish_reason == "tool_calls":
        for tc in choice.message.tool_calls or []:
            fn_name = tc.function.name
            args = json.loads(tc.function.arguments)
            print(f"도구 호출: {fn_name}({args})")
            if fn_name == "get_weather":
                result = get_weather(**args)
                print(f"함수 결과: {result}")
    else:
        print(choice.message.content)


if __name__ == "__main__":
    main()
