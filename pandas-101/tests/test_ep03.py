from __future__ import annotations

import importlib


def test_ep03_behavior() -> None:
    mod = importlib.import_module("en.ep03_read_csv_excel")
    out = mod.run()["ep03"]
    assert out["csv_shape"] == (3, 3)
    assert out["excel_shape"] == (3, 3)
    assert out["columns"] == ["id", "name", "value"]
