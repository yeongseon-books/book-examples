# Save all conversations to long-term memory
def save_conversation(user_id, messages):
    for msg in messages:
        long_term_memory.add(user_id, msg["content"])
# Greetings like "Hi", "Thanks" all saved
