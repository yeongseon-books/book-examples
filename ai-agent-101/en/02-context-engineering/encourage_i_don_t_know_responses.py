"""Generated from book-content article."""

def check_knowledge_boundary(query: str, knowledge_base: dict) -> str:
    """
    Checks if query is within knowledge scope.
    
    Answerable conditions:
    1. Related documentation exists in knowledge_base
    2. Query is within permission scope
    3. Information is current
    """
    if query not in knowledge_base:
        return "Cannot find official documentation for this question. Please contact HR team."
    
    doc = knowledge_base[query]
    if doc["restricted"]:
        return "This information requires restricted access permissions."
    
    if doc["outdated"]:
        return f"{doc['content']} (Warning: This information was last updated on {doc['last_updated']})"
    
    return doc["content"]
