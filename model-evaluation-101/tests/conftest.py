from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def load_module(rel_path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {rel_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
