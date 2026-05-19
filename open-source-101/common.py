"""Shared utilities and domain models for Open Source 101."""

from __future__ import annotations

import json
import re
import tempfile
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

SPDX_PATTERNS: dict[str, re.Pattern[str]] = {
    "MIT": re.compile(r"spdx-license-identifier:\s*mit", re.IGNORECASE),
    "Apache-2.0": re.compile(r"spdx-license-identifier:\s*apache-2\.0", re.IGNORECASE),
    "GPL-3.0-only": re.compile(
        r"spdx-license-identifier:\s*gpl-3\.0-only", re.IGNORECASE
    ),
}


def detect_spdx_license(license_text: str) -> str:
    """Detect spdx license."""
    for spdx, pattern in SPDX_PATTERNS.items():
        if pattern.search(license_text):
            return spdx
    return "UNKNOWN"


COMPATIBILITY = {
    ("MIT", "MIT"): True,
    ("MIT", "Apache-2.0"): True,
    ("MIT", "GPL-3.0-only"): True,
    ("Apache-2.0", "Apache-2.0"): True,
    ("Apache-2.0", "GPL-3.0-only"): False,
    ("GPL-3.0-only", "GPL-3.0-only"): True,
}


def is_license_compatible(project_license: str, dependency_license: str) -> bool:
    """Is license compatible."""
    return COMPATIBILITY.get((project_license, dependency_license), False)


def parse_markdown_front_matter(text: str) -> dict[str, str]:
    """Parse markdown front matter."""
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}
    result: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


def validate_pr_description(text: str) -> list[str]:
    """Validate pr description."""
    errors: list[str] = []
    if not re.search(r"Closes\s+#\d+", text):
        errors.append("missing_closes")
    if "## Summary" not in text:
        errors.append("missing_summary")
    checklist_items = re.findall(r"^- \[(?: |x)\]", text, flags=re.MULTILINE)
    if len(checklist_items) < 2:
        errors.append("missing_checklist")
    return errors


def score_readme(text: str) -> int:
    """Score readme."""
    required = ["install", "usage", "contributing", "license"]
    lowered = text.lower()
    score = 0
    for section in required:
        if section in lowered:
            score += 25
    return score


SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def parse_semver(version: str) -> tuple[int, int, int]:
    """Parse semver."""
    m = SEMVER_RE.match(version)
    if not m:
        raise ValueError(f"Invalid semver: {version}")
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def bump_semver(version: str, part: str) -> str:
    """Bump semver."""
    major, minor, patch = parse_semver(version)
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    if part == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError("part must be major/minor/patch")


def validate_contributing_files(
    contributing_text: str, has_coc: bool
) -> dict[str, bool]:
    """Validate contributing files."""
    return {
        "has_steps": "pull request" in contributing_text.lower(),
        "has_code_of_conduct": has_coc,
    }


@dataclass
class Issue:
    """Issue."""

    id: int
    title: str
    labels: list[str]


def triage_issues(issues: Iterable[Issue]) -> dict[str, int]:
    """Triage issues."""
    summary = {"bug": 0, "enhancement": 0, "question": 0, "other": 0}
    for issue in issues:
        mapped = "other"
        if "bug" in issue.labels:
            mapped = "bug"
        elif "enhancement" in issue.labels:
            mapped = "enhancement"
        elif "question" in issue.labels:
            mapped = "question"
        summary[mapped] += 1
    return summary


def score_portfolio(repos_json: str) -> int:
    """Score portfolio."""
    repos = json.loads(repos_json)
    score = 0
    for repo in repos:
        score += min(repo.get("stargazers_count", 0), 100)
        if repo.get("updated_days_ago", 365) <= 30:
            score += 20
    return score


def initialize_python_project(package_name: str) -> Path:
    """Initialize python project."""
    base = Path(tempfile.mkdtemp(prefix="os101-init-"))
    pkg_dir = base / package_name
    tests_dir = base / "tests"
    pkg_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)
    (pkg_dir / "__init__.py").write_text('__version__ = "0.1.0"\n', encoding="utf-8")
    (pkg_dir / "core.py").write_text(
        'def hello():\n    return "hello"\n', encoding="utf-8"
    )
    (tests_dir / "test_core.py").write_text(
        f'from {package_name}.core import hello\n\n\ndef test_hello():\n    assert hello() == "hello"\n',
        encoding="utf-8",
    )
    (base / "pyproject.toml").write_text(
        '[project]\nname = "' + package_name + '"\nversion = "0.1.0"\n',
        encoding="utf-8",
    )
    return base
