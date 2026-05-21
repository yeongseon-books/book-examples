# Search long-term memory every message
def run_agent(user_message):
    preferences = long_term_memory.retrieve(user_id)  # Repeated DB queries
    context = build_context(preferences, user_message)
    response = llm.generate(context)
    return response
