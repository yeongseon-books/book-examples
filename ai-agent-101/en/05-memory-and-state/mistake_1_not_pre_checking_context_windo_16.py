"""Generated from book-content article."""

import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o")

def count_tokens(messages):
    total = sum(len(encoding.encode(msg["content"])) for msg in messages)
    return total

# Check token count before adding message
if count_tokens(messages) + len(encoding.encode(user_input)) < 7000:
    messages.append({"role": "user", "content": user_input})
else:
    # Remove old messages
    messages = [messages[0]] + messages[-5:]
    messages.append({"role": "user", "content": user_input})
