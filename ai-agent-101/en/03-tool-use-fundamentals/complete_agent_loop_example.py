"""Generated from book-content article."""

from typing import Dict, Any, List
import openai
import json

def agent_with_tools(
    user_query: str,
    tools: List[Dict[str, Any]],
    max_iterations: int = 5
) -> str:
    """Agent loop with tool support."""
    
    messages = [{"role": "user", "content": user_query}]
    
    for iteration in range(max_iterations):
        # Call LLM
        response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        assistant_message = response.choices[0].message
        
        # Check if LLM wants to use a tool
        if not assistant_message.tool_calls:
            # No tool call = final answer ready
            return assistant_message.content
        
        # Add assistant's tool call to conversation
        messages.append(assistant_message)
        
        # Execute each tool call
        for tool_call in assistant_message.tool_calls:
            tool_name = tool_call.function.name
            tool_args = tool_call.function.arguments
            
            # Execute tool
            result = execute_tool(tool_name, tool_args)
            
            # Add result to conversation
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })
    
    return "Max iterations reached without completion."

# Example usage
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Retrieves current weather information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }
]

answer = agent_with_tools("What's the weather in Seoul?", tools)
print(answer)
