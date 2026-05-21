"""Generated from book-content article."""

ALLOWED_SORT_FIELDS = {"created_at", "updated_at", "name", "price"}

def parse_sort(raw: str) -> list[tuple[str, str]]:
    """'created_at:desc,name:asc' → [('created_at', 'desc'), ('name', 'asc')]"""
    result = []
    for part in raw.split(","):
        field, _, direction = part.partition(":")
        if field not in ALLOWED_SORT_FIELDS:
            raise ValueError(f"정렬 불가: {field}")
        direction = direction or "asc"
        if direction not in ("asc", "desc"):
            raise ValueError(f"잘못된 방향: {direction}")
        result.append((field, direction))
    return result
