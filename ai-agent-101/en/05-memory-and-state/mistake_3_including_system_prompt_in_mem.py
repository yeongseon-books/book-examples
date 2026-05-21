# Remove system prompt along with others
def trim_messages(messages):
    return messages[-5:]  # System prompt may disappear
