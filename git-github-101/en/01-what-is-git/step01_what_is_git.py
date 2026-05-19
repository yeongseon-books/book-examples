from __future__ import annotations

from pathlib import Path
import importlib.util


def _load_run() -> object:
    path = (
        Path(__file__).resolve().parents[2] / "ko/01-what-is-git/step01_what_is_git.py"
    )
    spec = importlib.util.spec_from_file_location("ko_ep01", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.run


run = _load_run()
