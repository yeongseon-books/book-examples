# Add messages without checking token count
messages.append({"role": "user", "content": user_input})
response = client.chat.completions.create(model="gpt-4o", messages=messages)
# Error when context window exceeded
