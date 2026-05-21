"""Generated from book-content article."""

def record_llm_call(span: Span, prompt: str, model: str, response: str, usage: dict):
    span.attributes.update({
        "llm.model": model,
        "llm.prompt_tokens": usage["prompt_tokens"],
        "llm.completion_tokens": usage["completion_tokens"],
        "llm.cost_usd": _calculate_cost(model, usage),
    })
    span.events.append({
        "name": "llm.prompt",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "body": prompt,
    })
    span.events.append({
        "name": "llm.response",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "body": response,
    })
