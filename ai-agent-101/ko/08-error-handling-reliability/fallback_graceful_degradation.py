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
