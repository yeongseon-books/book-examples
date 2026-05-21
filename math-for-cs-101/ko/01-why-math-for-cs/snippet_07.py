"""Generated from book-content article."""

from collections.abc import Iterable


def unique_positive(values: Iterable[int]) -> list[int]:
    # 조건: 양의 정수만 남기고 중복 제거
    s = {x for x in values if x > 0}
    return sorted(s)
