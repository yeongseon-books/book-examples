def collection_summary(
    values: list[int], weights: dict[str, int], nums: tuple[int, ...], tags: set[str]
) -> dict[str, int]:
    return {
        "values_total": sum(values),
        "weight_total": sum(weights.values()),
        "nums_total": sum(nums),
        "tag_count": len(tags),
    }
