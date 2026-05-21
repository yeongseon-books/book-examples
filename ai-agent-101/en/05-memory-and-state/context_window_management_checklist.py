# Token usage logging example
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages
)

usage = response.usage
print(f"Prompt tokens: {usage.prompt_tokens}")
print(f"Completion tokens: {usage.completion_tokens}")
print(f"Total tokens: {usage.total_tokens}")

# Cost calculation (GPT-4: $0.03/1K prompt tokens, $0.06/1K completion tokens)
cost = (usage.prompt_tokens / 1000 * 0.03) + (usage.completion_tokens / 1000 * 0.06)
print(f"Cost: ${cost:.4f}")
