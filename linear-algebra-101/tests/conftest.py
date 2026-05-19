import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def load_episode(ep: str):
    path = ROOT / 'en' / ep / 'step01_example.py'
    spec = importlib.util.spec_from_file_location(f'ep_{ep.replace("-", "_")}', path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module
