"""Type Hints Python 101 - Episode 2: Basic collections."""


def collection_summary(
    values: list[int], weights: dict[str, int], nums: tuple[int, ...], tags: set[str]
) -> dict[str, int]:
    """Collection summary."""
    return {
        "values_total": sum(values),
        "weight_total": sum(weights.values()),
        "nums_total": sum(nums),
        "tag_count": len(tags),
    }
