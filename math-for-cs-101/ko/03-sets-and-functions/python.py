"""Generated from book-content article."""

def resolve_permissions(allowed: set[str], requested: set[str], blocked: set[str]) -> set[str]:
    return (allowed & requested) - blocked

allowed = {"read", "write", "delete", "audit"}
requested = {"read", "delete"}
blocked = {"delete"}
print(resolve_permissions(allowed, requested, blocked))  # {'read'}
