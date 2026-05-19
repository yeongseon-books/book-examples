"""Shared utilities and domain models for Software Engineering 101."""

from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Any

SECTION_HEADERS = [
    "## Context",
    "## Problem",
    "## Goals",
    "## Non-Goals",
    "## Design",
    "## Rollout",
]


def read_text(path: str | Path) -> str:
    """Read text."""
    return Path(path).read_text(encoding="utf-8")


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    """Parse markdown table."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    rows = [line for line in lines if line.startswith("|") and line.endswith("|")]
    if len(rows) < 2:
        return []
    headers = [h.strip() for h in rows[0].strip("|").split("|")]
    items = []
    for row in rows[2:]:
        cols = [c.strip() for c in row.strip("|").split("|")]
        if len(cols) != len(headers):
            continue
        items.append(dict(zip(headers, cols, strict=False)))
    return items


def semver_bump(version: str, part: str) -> str:
    """Semver bump."""
    major, minor, patch = [int(v) for v in version.split(".")]
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    if part == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError("part must be major|minor|patch")


def python_functions_with_docstrings(code: str) -> tuple[int, int]:
    """Python functions with docstrings."""
    tree = ast.parse(code)
    funcs = [
        n
        for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef | ast.AsyncFunctionDef)
    ]
    with_docs = sum(1 for f in funcs if ast.get_docstring(f))
    return len(funcs), with_docs


def todo_count(text: str) -> dict[str, int]:
    """Todo count."""
    return {
        "TODO": len(re.findall(r"\bTODO\b", text)),
        "FIXME": len(re.findall(r"\bFIXME\b", text)),
    }


def readability_score(lines: list[str]) -> float:
    """Readability score."""
    if not lines:
        return 0.0
    avg_len = mean(len(l) for l in lines)
    return max(0.0, 100.0 - (avg_len * 0.6))


def dump_json(data: dict[str, Any]) -> str:
    """Dump json."""
    return json.dumps(data, indent=2, ensure_ascii=False)


@dataclass
class BranchMachine:
    """Branch machine."""

    state: str = "main"

    def apply(self, event: str) -> str:
        """Apply."""
        transitions = {
            ("main", "feature_start"): "feature",
            ("feature", "open_pr"): "review",
            ("review", "merge"): "main",
            ("feature", "abort"): "main",
        }
        key = (self.state, event)
        if key not in transitions:
            raise ValueError(f"invalid transition: {self.state} -> {event}")
        self.state = transitions[key]
        return self.state
