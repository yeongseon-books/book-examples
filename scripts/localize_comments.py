"""Localize inline comments in ko/ Python files to Korean.

Translates common English comment patterns to Korean equivalents.
Preserves code structure and only modifies comment text.
"""

from __future__ import annotations

import re
from pathlib import Path


BOOK_EXAMPLES_ROOT = Path("/data/GitHub/book-examples")

# Common comment translations (English → Korean)
COMMENT_TRANSLATIONS = {
    # File markers
    "# English mirror": "",
    "# Generated from book-content article.": "# book-content 본문에서 생성된 코드입니다.",
    # Common patterns
    "# Example": "# 예시",
    "# example": "# 예시",
    "# Demo": "# 데모",
    "# demo": "# 데모",
    "# Main": "# 메인",
    "# main": "# 메인",
    "# Test": "# 테스트",
    "# test": "# 테스트",
    "# Config": "# 설정",
    "# config": "# 설정",
    "# Configuration": "# 설정",
    "# configuration": "# 설정",
    "# Setup": "# 설정",
    "# setup": "# 설정",
    "# Initialize": "# 초기화",
    "# initialize": "# 초기화",
    "# Create": "# 생성",
    "# create": "# 생성",
    "# Delete": "# 삭제",
    "# delete": "# 삭제",
    "# Update": "# 업데이트",
    "# update": "# 업데이트",
    "# Read": "# 읽기",
    "# Result": "# 결과",
    "# result": "# 결과",
    "# Output": "# 출력",
    "# output": "# 출력",
    "# Input": "# 입력",
    "# input": "# 입력",
    "# Return": "# 반환",
    "# return": "# 반환",
    "# Error": "# 오류",
    "# error": "# 오류",
    "# Warning": "# 경고",
    "# Note": "# 참고",
    "# note": "# 참고",
    "# TODO": "# TODO",
    "# FIXME": "# FIXME",
}

# Regex-based translations for parameterized comments
COMMENT_PATTERNS = [
    # "# Step N: description" → "# N단계: description"
    (r"# Step (\d+):", r"# \1단계:"),
    # "# Example: ..." → "# 예시: ..."
    (r"# Example:", "# 예시:"),
    # "# Returns ..." → "# 반환: ..."
    (r"# Returns? ", "# 반환: "),
    # "# See also: ..." → "# 참고: ..."
    (r"# See also:", "# 참고:"),
    # "# Expected output:" → "# 예상 출력:"
    (r"# Expected output:?", "# 예상 출력:"),
    # "# Run:" → "# 실행:"
    (r"# Run:", "# 실행:"),
    # "# Usage:" → "# 사용법:"
    (r"# Usage:", "# 사용법:"),
]


def translate_comment_line(line: str) -> str:
    """Translate a single comment line from English to Korean."""
    stripped = line.rstrip()

    # Check if this line has an inline comment (code + # comment)
    # Only process pure comment lines (starting with #) or inline comments
    # For inline comments: preserve code, translate comment
    code_part = ""
    comment_part = stripped

    if not stripped.lstrip().startswith("#"):
        # Check for inline comment
        # Simple heuristic: find # that's not inside a string
        in_string = False
        string_char = None
        for idx, ch in enumerate(stripped):
            if ch in ('"', "'") and (idx == 0 or stripped[idx - 1] != "\\"):
                if not in_string:
                    in_string = True
                    string_char = ch
                elif ch == string_char:
                    in_string = False
            elif ch == "#" and not in_string:
                code_part = stripped[:idx]
                comment_part = stripped[idx:]
                break
        else:
            return line  # No comment found

    # Try exact matches first
    for eng, kor in COMMENT_TRANSLATIONS.items():
        if comment_part.strip() == eng:
            if kor == "":
                return ""  # Remove line entirely
            indent = len(line) - len(line.lstrip())
            return " " * indent + code_part + kor

    # Try regex patterns
    for pattern, replacement in COMMENT_PATTERNS:
        new_comment = re.sub(pattern, replacement, comment_part)
        if new_comment != comment_part:
            indent = len(line) - len(line.lstrip())
            return " " * indent + code_part + new_comment

    return line


def localize_file(filepath: Path) -> bool:
    """Localize comments in a Python file to Korean. Returns True if modified."""
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")
    new_lines = []
    modified = False

    for line in lines:
        new_line = translate_comment_line(line)
        if new_line != line:
            modified = True
        if new_line != "":  # Skip removed lines
            new_lines.append(new_line)
        elif new_line == "" and line.strip() == "":
            new_lines.append(line)  # Preserve blank lines

    if modified:
        filepath.write_text("\n".join(new_lines), encoding="utf-8")

    return modified


def process_series(series: str) -> int:
    """Process all ko/ files in a series. Returns count of modified files."""
    ko_dir = BOOK_EXAMPLES_ROOT / series / "ko"
    if not ko_dir.exists():
        return 0

    modified_count = 0
    for py_file in sorted(ko_dir.rglob("*.py")):
        if "__pycache__" in str(py_file):
            continue
        if localize_file(py_file):
            modified_count += 1

    return modified_count


def main() -> None:
    """Main entry."""
    import argparse

    parser = argparse.ArgumentParser(description="Localize ko/ comments to Korean")
    parser.add_argument("series", nargs="*")
    args = parser.parse_args()

    default_series = [
        "ai-agent-101",
        "ai-data-preparation-101",
        "ai-evaluation-101",
        "ai-safety-guardrails-101",
        "alembic-101",
        "api-design-101",
        "backend-development-101",
        "calculus-for-ml-101",
        "capstone-project-101",
        "frontend-development-101",
        "git-github-101",
        "github-actions-101",
        "harness-engineering-101",
        "incident-response-101",
        "kubernetes-101",
        "linear-algebra-101",
        "linux-cli-101",
        "llm-from-scratch-101",
        "math-for-cs-101",
        "model-evaluation-101",
        "multimodal-ai-101",
    ]

    series_list = args.series or default_series
    total = 0

    for series in series_list:
        n = process_series(series)
        if n:
            print(f"{series}: {n} files localized")
        total += n

    print(f"\nTotal: {total} files localized")


if __name__ == "__main__":
    main()
