"""Portfolio Project 101 - Episode 7: Adr parser."""

from __future__ import annotations

from common import extract_markdown_sections, parse_front_matter


def parse_adr(md_text: str) -> dict[str, object]:
    """Parse adr."""
    front = parse_front_matter(md_text)
    sections = extract_markdown_sections(md_text)
    required = {"Context", "Decision", "Consequences"}
    return {
        "front_matter": front,
        "sections": sorted(sections),
        "is_valid": required.issubset(sections) and bool(front),
    }
