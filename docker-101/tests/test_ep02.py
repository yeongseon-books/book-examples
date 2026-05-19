# pyright: reportAny=false
from conftest import load_module

run = load_module(
    "ko/02-image-and-container/step01_image_container_lifecycle.py", "ep02"
).run


def test_ep02() -> None:
    result = run()
    assert result["success"] is True
    assert result["lifecycle"][-1] == "removed"
