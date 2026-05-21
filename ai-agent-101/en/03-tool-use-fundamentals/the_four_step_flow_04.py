# Add tool result to conversation
messages = [
    {"role": "user", "content": "What's the weather in Seoul?"},
    response.choices[0].message,  # Assistant's tool call
    {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result  # Tool execution result
    }
]

# Get final answer
final_response = openai.chat.completions.create(
    model="gpt-4.1",
    messages=messages
)

print(final_response.choices[0].message.content)
# Output: "The current weather in Seoul is sunny with a temperature of 15°C."
