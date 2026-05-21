"""Generated from book-content article."""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[...],
    temperature=0,
    seed=42,  # OpenAI seed parameter
)
