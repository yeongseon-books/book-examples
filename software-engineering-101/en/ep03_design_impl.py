"""Software Engineering 101 - Episode 3: Design impl."""

from __future__ import annotations

from common import SECTION_HEADERS


def design_doc_completeness(text: str) -> dict[str, object]:
    """Design doc completeness."""
    present = {header: (header in text) for header in SECTION_HEADERS}
    score = sum(present.values()) / len(SECTION_HEADERS)
    return {"present": present, "score": round(score, 2)}


def generate_impl_skeleton(feature_name: str) -> str:
    """Generate impl skeleton."""
    return f"""def implement_{feature_name}(input_data):
    \"\"\"Implementation skeleton generated from design checkpoint.\"\"\"
    raise NotImplementedError(\"define business logic\")
"""
