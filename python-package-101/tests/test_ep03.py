from pathlib import Path

from common import ep03_parse_dependencies


def test_ep03_parse_pep508_dependencies() -> None:
    out = ep03_parse_dependencies(Path("fixtures/sample_pyproject.toml"))
    assert len(out) >= 2
    assert out[0]["valid"] is True
    assert out[1]["marker"] is not None
