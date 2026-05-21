# Bad
response = openai.ChatCompletion.create(...)  # zero cost tracking
return response

# Good
response = openai.ChatCompletion.create(...)
budget.record(
    user_id=current_user,
    model=response.model,
    prompt_tokens=response.usage.prompt_tokens,
    completion_tokens=response.usage.completion_tokens
)
