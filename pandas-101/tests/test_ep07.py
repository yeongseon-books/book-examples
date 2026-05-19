from __future__ import annotations

import importlib


def test_ep07_behavior() -> None:
    mod = importlib.import_module("en.ep07_merge_join_concat")
    out = mod.run()["ep07"]
    assert out["inner_shape"] == (2, 3)
    assert out["outer_shape"][0] == 4
    assert out["concat_shape"][0] == 6
