from pathlib import Path
from typing import Any, cast

from common import read_text
from ko.ep07_adr_parser import parse_adr


def test_ep07_adr_parser() -> None:
    parsed = cast(
        "dict[str, Any]", parse_adr(read_text(Path("fixtures/sample_adr.md")))
    )
    assert parsed["is_valid"] is True
    assert parsed["front_matter"]["id"] == "ADR-001"
