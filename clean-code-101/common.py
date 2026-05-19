from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import importlib.util
from types import ModuleType


@dataclass(frozen=True)
class Item:
    name: str
    price: int
    qty: int


def load_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
