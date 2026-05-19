from __future__ import annotations

import importlib


def test_ep10_behavior() -> None:
    mod = importlib.import_module("en.ep10_end_to_end_analysis")
    out = mod.run()["ep10"]
    assert out["insights_rows"] > 0
    assert out["total_revenue"] > 0
    assert isinstance(out["top_region"], str)
