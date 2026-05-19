from __future__ import annotations

import importlib.util
from pathlib import Path


def load_module(script_name: str):
    path = Path(__file__).resolve().parents[1] / "ko" / script_name
    spec = importlib.util.spec_from_file_location(script_name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module
