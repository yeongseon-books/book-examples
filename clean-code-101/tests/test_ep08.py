import importlib.util
from datetime import datetime
from pathlib import Path


def load(path: str):
    module_path = Path(__file__).resolve().parent.parent / "ko" / path
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep08_testability() -> None:
    m = load("08-testable-code/step01_testable_code.py")
    due = datetime(2025, 1, 1)
    now = datetime(2025, 1, 2)
    assert m.is_overdue(due, now=now) is True
    repo = m.FakeRepo()
    user = {"id": "u1", "name": "Kim"}
    m.register(repo, user)
    assert repo.get("u1") == user
