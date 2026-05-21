"""Generated from book-content article."""

class FallbackChain:
    """Try fallbacks sequentially."""

    def __init__(self):
        self.handlers = []

    def add(self, handler: Callable, name: str):
        self.handlers.append((name, handler))
        return self

    def execute(self, *args, **kwargs):
        errors = []
        for name, handler in self.handlers:
            try:
                result = handler(*args, **kwargs)
                return {"result": result, "source": name, "fallbacks_tried": errors}
            except Exception as e:
                errors.append({"handler": name, "error": str(e)})
        raise RuntimeError(f"all handlers failed: {errors}")

# Example usage
def primary_search(query):
    return external_search_api(query)

def cached_search(query):
    return cache.get(f"search:{query}") or []

def degraded_search(query):
    return [{"text": f"Search for '{query}' is temporarily unavailable.", "fallback": True}]

chain = (FallbackChain()
    .add(primary_search, "primary")
    .add(cached_search, "cache")
    .add(degraded_search, "degraded"))

result = chain.execute("Python tutorial")
# On primary failure → cache; on cache failure → friendly message
