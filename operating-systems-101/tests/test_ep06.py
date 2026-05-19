from typing import Any, cast

from common import ep06_first_fit_allocator


def test_ep06_allocator_first_fit():
    out = cast("dict[str, Any]", ep06_first_fit_allocator(20, [5, 6, 12]))
    assert out["allocated"][0] == (0, 5)
    assert out["allocated"][1] == (5, 6)
    assert out["allocated"][2][0] == -1
