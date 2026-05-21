"""Generated from book-content article."""

from typing import Any, Dict, List

import openai


def react_agent(user_query: str, tools: list[dict], max_steps: int = 10) -> str:
    """ReAct pattern: Thought → Action → Observation loop"""

    messages = [
        {"role": "system", "content": """You are an agent that solves problems step-by-step.\n\n        At each step:\n        1. Thought: Think about what to do next\n        2. Action: Use tools to gather information\n        3. Observation: Observe results and plan next step\n\n        When you reach the goal, provide an answer starting with "Final Answer:"."""},
        {"role": "user", "content": user_query}
    ]

    for _step in range(max_steps):
        # Request next action from LLM
        response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        assistant_message = response.choices[0].message

        # If final answer
        if assistant_message.content and "Final Answer:" in assistant_message.content:
            return assistant_message.content.replace("Final Answer:", "").strip()

        # If tool call
        if assistant_message.tool_calls:
            messages.append(assistant_message)

            # Execute each tool
            for tool_call in assistant_message.tool_calls:
                result = execute_tool(tool_call.function.name, tool_call.function.arguments)

                # Add observation
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": f"Observation: {result}"
                })
        else:
            # Neither tool call nor final answer
            messages.append(assistant_message)

    return "Max steps reached without solution."
