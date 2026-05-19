from __future__ import annotations

import importlib


def test_ep04_behavior() -> None:
    mod = importlib.import_module("en.ep04_boolean_query")
    out = mod.run()["ep04"]
    assert out["filter_count"] >= 0
    assert out["query_count"] >= 0
    assert out["isin_count"] >= out["query_count"]
