"""Generated from book-content article."""

import openai

tools = [
    {"type": "function", "function": {...}},  # get_weather
    {"type": "function", "function": {...}},  # search_documents
]

# Strategy 1: Automatic selection (LLM decides)
response = openai.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "What's the weather in Seoul?"}],
    tools=tools,
    tool_choice="auto"  # LLM uses tools when needed
)

# Strategy 2: Force tool use
response = openai.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "What's the weather in Seoul?"}],
    tools=tools,
    tool_choice="required"  # Must call one tool
)

# Strategy 3: Specify tool
response = openai.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "What's the weather in Seoul?"}],
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "get_weather"}}
)

# Strategy 4: Disable tools
response = openai.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "What's the weather in Seoul?"}],
    tools=tools,
    tool_choice="none"  # No tool use
)
