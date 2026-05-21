# Good example
def build_context(history: list, max_tokens: int = 4000) -> list:
    """Builds context considering token limits."""
    context = []
    token_count = 0
    
    # Add recent messages in reverse order
    for msg in reversed(history):
        msg_tokens = estimate_tokens(msg["content"])
        if token_count + msg_tokens > max_tokens:
            break
        context.insert(0, msg)
        token_count += msg_tokens
    
    return context
