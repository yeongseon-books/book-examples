# Bad
def search(query):
    return external_api.search(query)  # If the API dies, everything dies

# Good
def search(query):
    try:
        return external_api.search(query)
    except Exception:
        return cache.get(query) or []  # At least serve cache
