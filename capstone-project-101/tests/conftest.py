from __future__ import annotations
import importlib.util
from pathlib import Path
from types import ModuleType

def load_module(path: str, name: str) -> ModuleType:
    module_path = Path(__file__).resolve().parent.parent / path
    spec = importlib.util.spec_from_file_location(name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Cannot load module: {path}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
