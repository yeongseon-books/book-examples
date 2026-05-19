from __future__ import annotations

from common import parse_markdown_table


def invest_checklist(markdown_text: str) -> list[dict[str, object]]:
    rows = parse_markdown_table(markdown_text)
    out = []
    for row in rows:
        checks = {
            "independent": bool(row.get("role")),
            "negotiable": len(row.get("goal", "")) > 3,
            "valuable": bool(row.get("benefit")),
            "estimable": len(row.get("goal", "")) < 80,
            "small": len(row.get("goal", "").split()) <= 8,
            "testable": row.get("goal", "").startswith(
                ("reset", "export", "create", "update")
            ),
        }
        out.append(
            {
                "story": row.get("story", ""),
                "checks": checks,
                "score": sum(checks.values()),
            }
        )
    return out
