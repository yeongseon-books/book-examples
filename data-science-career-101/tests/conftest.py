from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load_module(path: str):
    module_path = Path(path)
    spec = importlib.util.spec_from_file_location(
        module_path.stem.replace("-", "_"), module_path
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
