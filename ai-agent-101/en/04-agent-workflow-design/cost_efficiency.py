# Bad: LLM call for each item
def inefficient_workflow(items: List[str]) -> List[str]:
    """Inefficient: call LLM per item"""
    results = []
    for item in items:
        result = llm_call(f"Process this: {item}")  # $0.01 each
        results.append(result)
    return results
    # 100 items = $1.00

# Good: batch processing
def efficient_workflow(items: List[str]) -> List[str]:
    """Efficient: batch items together"""
    batch_prompt = f"""
    Process each of the following items:
    {chr(10).join(f"{i+1}. {item}" for i, item in enumerate(items))}
    """
    
    response = llm_call(batch_prompt)  # Single call: $0.05
    results = parse_batch_response(response)
    return results
    # 100 items = $0.05 (95% savings)
