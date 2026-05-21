"""Generated from book-content article."""

def multi_tool_workflow(user_query: str) -> str:
    """Generate answer by combining multiple tools."""

    # Step 1: Search documents
    search_result = execute_tool("search_documents", {"query": user_query})

    if not search_result["success"]:
        return "Search failed"

    documents = search_result["data"]

    # Step 2: Pass documents to LLM for summarization
    summary_prompt = f"""
    Answer the question based on these documents.

    Question: {user_query}

    Documents:
    {documents}
    """

    response = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": summary_prompt}]
    )

    return response.choices[0].message.content
