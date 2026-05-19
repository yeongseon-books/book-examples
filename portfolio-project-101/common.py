from __future__ import annotations

import ast
import json
import re
from pathlib import Path
from typing import Any


def clamp_score(value: int, low: int = 0, high: int = 100) -> int:
    return max(low, min(high, int(value)))


def read_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def read_json(path: str | Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def contains_port_binding(text: str) -> bool:
    return "0.0.0.0" in text


def list_py_files(root: str | Path) -> list[Path]:
    return sorted(Path(root).rglob("*.py"))


def count_docstrings(path: str | Path) -> int:
    tree = ast.parse(read_text(path))
    count = 1 if ast.get_docstring(tree) else 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef):
            if ast.get_docstring(node):
                count += 1
    return count


def extract_markdown_sections(md_text: str) -> set[str]:
    sections: set[str] = set()
    for line in md_text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            sections.add(m.group(1).strip())
    return sections


def parse_front_matter(md_text: str) -> dict[str, str]:
    lines = md_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line == "---":
            break
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out
