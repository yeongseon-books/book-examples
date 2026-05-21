# Fetching too much information exceeds context window
relevant_memories = vector_store.search_memory(
    user_id="user123",
    query=query,
    top_k=3  # Top 3 only
)

# Time range limit
recent_summaries = structured_store.get_recent_summaries(
    user_id="user123",
    limit=5  # Recent 5 sessions only
)
