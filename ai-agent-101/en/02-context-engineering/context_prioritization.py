"""Generated from book-content article."""

def assemble_context(
    system_prompt: str,
    user_query: str,
    conversation_history: list,
    retrieved_docs: list,
    current_state: dict
) -> str:
    """Assembles context according to priority."""

    # Priority order:
    # 1. System prompt (always top)
    # 2. Current task state (most important)
    # 3. Retrieved documents (latest info)
    # 4. Recent conversation (summarize or remove old ones)
    # 5. User query (last)

    context_parts = [
        f"# System Prompt\n{system_prompt}",
        f"\n# Current State\n{format_state(current_state)}",
        f"\n# Retrieved Documents\n{format_docs(retrieved_docs)}",
        f"\n# Recent Conversation\n{format_history(conversation_history[-5:])}",  # Last 5 only
        f"\n# User Query\n{user_query}"
    ]

    return "\n\n".join(context_parts)

def format_state(state: dict) -> str:
    return f"Task: {state['task']}\nProgress: {state['completed']}/{state['total']}"

def format_docs(docs: list) -> str:
    return "\n".join([f"- {d['content'][:200]}..." for d in docs])

def format_history(history: list) -> str:
    return "\n".join([f"{msg['role']}: {msg['content']}" for msg in history])
