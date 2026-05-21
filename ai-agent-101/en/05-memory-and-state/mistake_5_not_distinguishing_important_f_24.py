"""Generated from book-content article."""

def save_conversation(user_id, messages):
    for msg in messages:
        # Save only important information (by length, keywords)
        if len(msg["content"]) > 50 and msg["role"] == "user":
            # Save only questions or requests
            if any(keyword in msg["content"] for keyword in ["?", "how", "what", "tell me", "method"]):
                long_term_memory.add(user_id, msg["content"])
