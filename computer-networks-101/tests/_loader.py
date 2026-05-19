import importlib.util
from pathlib import Path


def load_ko(slug: str):
    path = Path(__file__).resolve().parents[1] / "ko" / f"{slug}.py"
    spec = importlib.util.spec_from_file_location(slug.replace('-', '_'), path)
    if spec is None or spec.loader is None:
        raise ImportError(f"unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
