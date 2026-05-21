"""Generated from book-content article."""

def stream_with_budget(prompt: str, user_id: str, max_output: int):
    bucket_key = f"u:{user_id}:out"
    spent = 0
    for chunk in llm.stream(prompt, max_tokens=max_output):
        token_count = len(chunk.split())  # use a real tokenizer in production
        if not token_bucket(bucket_key, capacity=200_000, refill_per_sec=200_000/60, cost=token_count):
            yield "[output quota exceeded]"
            return
        spent += token_count
        yield chunk
