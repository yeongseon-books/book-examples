"""Localize genuine code comments in ko/ Python files to Korean.

Only translates comments that are clearly instructional/code-flow comments.
Leaves output examples, data strings, and technical identifiers untouched.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path("/data/GitHub/book-examples")

# Exact full-comment translations (case-insensitive match after "# ")
EXACT_MAP: dict[str, str] = {
    "execute tool": "도구 실행",
    "verify": "검증",
    "verification": "검증",
    "validate": "검증",
    "initialize": "초기화",
    "cleanup": "정리",
    "setup": "설정",
    "set up": "설정",
    "fallback": "폴백",
    "retry": "재시도",
    "simple": "간단한 방식",
    "basic": "기본",
    "advanced": "고급",
    "optional": "선택사항",
    "required": "필수",
    "result": "결과",
    "output": "출력",
    "input": "입력",
    "helper": "헬퍼",
    "wrapper": "래퍼",
    "cache": "캐시",
    "placeholder": "플레이스홀더",
    "dummy": "더미",
    "mock": "모의",
}

# Prefix-based translations: if comment starts with pattern, translate
PREFIX_MAP: list[tuple[re.Pattern, callable]] = [
    (
        re.compile(r"^Wrong[:.]?\s*(.*)$", re.I),
        lambda m: f"잘못된 방식: {m.group(1)}" if m.group(1) else "잘못된 방식",
    ),
    (
        re.compile(r"^Right[:.]?\s*(.*)$", re.I),
        lambda m: f"올바른 방식: {m.group(1)}" if m.group(1) else "올바른 방식",
    ),
    (
        re.compile(r"^Correct[:.]?\s*(.*)$", re.I),
        lambda m: f"올바른 방식: {m.group(1)}" if m.group(1) else "올바른 방식",
    ),
    (
        re.compile(r"^Stage (\d+)[:.]?\s*(.*)$", re.I),
        lambda m: (
            f"{m.group(1)}단계: {m.group(2)}" if m.group(2) else f"{m.group(1)}단계"
        ),
    ),
    (
        re.compile(r"^Step (\d+)[:.]?\s*(.*)$", re.I),
        lambda m: (
            f"{m.group(1)}단계: {m.group(2)}" if m.group(2) else f"{m.group(1)}단계"
        ),
    ),
    (
        re.compile(r"^Phase (\d+)[:.]?\s*(.*)$", re.I),
        lambda m: (
            f"{m.group(1)}단계: {m.group(2)}" if m.group(2) else f"{m.group(1)}단계"
        ),
    ),
    (
        re.compile(r"^Validate at every stage entry$", re.I),
        lambda m: "각 단계 진입 시 검증",
    ),
    (re.compile(r"^Verify[:.]?\s*(.+)$", re.I), lambda m: f"검증: {m.group(1)}"),
    (re.compile(r"^Keep only (.+)$", re.I), lambda m: f"{m.group(1)}만 유지"),
    (re.compile(r"^Keep (.+)$", re.I), lambda m: f"{m.group(1)} 유지"),
    (re.compile(r"^Use (.+)$", re.I), lambda m: f"{m.group(1)} 사용"),
    (re.compile(r"^Assume (.+)$", re.I), lambda m: f"가정: {m.group(1)}"),
    (re.compile(r"^Normalize before (.+)$", re.I), lambda m: f"{m.group(1)} 전 정규화"),
    (re.compile(r"^Normalize (.+)$", re.I), lambda m: f"{m.group(1)} 정규화"),
    (re.compile(r"^Strip (.+)$", re.I), lambda m: f"{m.group(1)} 제거"),
    (
        re.compile(r"^Rolling[- ]window (.+)$", re.I),
        lambda m: f"롤링 윈도우 {m.group(1)}",
    ),
    (
        re.compile(r"^Canary detection \(simple\)$", re.I),
        lambda m: "카나리 탐지 (간단한 방식)",
    ),
    (
        re.compile(r"^True means (.+)$", re.I),
        lambda m: f"True는 {m.group(1)}을 의미합니다",
    ),
    (re.compile(r"^Pre-input$", re.I), lambda m: "사전 입력"),
    (
        re.compile(r"^Treat missing (.+) conservatively$", re.I),
        lambda m: f"누락된 {m.group(1)}을 보수적으로 처리",
    ),
]

# Whitelist patterns — never translate these
WHITELIST_RE = re.compile(
    r"^#\s*("
    r"pyright|type:|noqa|pylint|pragma|TODO|FIXME|NOTE|HACK|XXX|fmt:|isort:|"
    r"https?://|/[a-z]"  # URLs and file paths
    r")",
    re.I,
)

# Output/example patterns — never translate these
OUTPUT_RE = re.compile(
    r"^("
    r"Expected output|Response:|Assistant:|User:|Input:|Output:|"
    r"Tool call|Tool result|Epoch \d|Loss:|Router|Retrieved:|"
    r"Query:|Prompt:|Token|Step \d.*→|Turn \d|Node '|"
    r"Model saved|LoRA|Vector store|Training complete|"
    r"Confidence:|Classification:|Estimated cost|"
    r"Memory savings|Generated:|Attempt \d|"
    r"Agent:|Final:|Answer:|Daily usage|"
    r"Written \d|Weights sum|Vocabulary size|"
    r"Window size|Whisper|What changing|"
    r"ViT|Validation split|Validation passed|"
    r"Vary inputs|Counter\(|"
    r"[A-Z][a-z]+ → |"  # Flow arrows like "Router → agent"
    r"\"[^\"]+\"|'[^']+'"  # Quoted strings
    r")",
    re.I,
)

# String/data comments — these contain literal data, not instructions
DATA_RE = re.compile(
    r"("
    r"\{[^}]+\}|"  # JSON-like content
    r"\$\d|"  # Dollar amounts
    r"\d+°[FC]|"  # Temperatures
    r"[A-Z][a-z]+Error|"  # Exception names
    r"__label__|"  # fasttext labels
    r"\.jsonl|\.json|\.txt|\.csv|"  # File extensions
    r"KenLM|"
    r"Spanish|"  # Language identifiers in test data
    r"[a-z_]+\(|"  # function calls
    r"^\d+\.\d+"  # version numbers / floats
    r")"
)


def should_translate(comment_text: str) -> bool:
    """Determine if a comment should be translated."""
    stripped = comment_text.strip()
    if not stripped:
        return False
    # Already Korean
    if re.search(r"[\uac00-\ud7a3]", stripped):
        return False
    # Whitelist
    if WHITELIST_RE.match(f"# {stripped}"):
        return False
    # Output examples
    if OUTPUT_RE.match(stripped):
        return False
    # Data/string content
    if DATA_RE.search(stripped):
        return False
    # Single word that's likely a technical term — but allow if in EXACT_MAP
    if re.match(r"^[A-Za-z_]+$", stripped) and len(stripped) > 2:
        if stripped.lower() not in EXACT_MAP:
            return False
    return True


def translate_comment(comment_text: str) -> str | None:
    """Translate a comment. Returns None if no translation available."""
    stripped = comment_text.strip()
    lower = stripped.lower()

    # Exact match
    if lower in EXACT_MAP:
        return EXACT_MAP[lower]

    # Prefix patterns
    for pattern, translator in PREFIX_MAP:
        m = pattern.match(stripped)
        if m:
            return translator(m)

    # No confident translation available — leave as-is
    return None


def process_file(filepath: Path, dry_run: bool = False) -> int:
    """Process a single file. Returns count of translated comments."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.split("\n")
    changed = 0

    for i, line in enumerate(lines):
        # Find comment (standalone or inline)
        m = re.search(r"(^|\s+)#\s+(.+)$", line)
        if not m:
            continue

        comment_text = m.group(2)
        if not should_translate(comment_text):
            continue

        translation = translate_comment(comment_text)
        if translation is None:
            continue

        # Replace the comment text
        new_line = line[: m.start(2)] + translation
        if new_line != line:
            lines[i] = new_line
            changed += 1

    if changed > 0 and not dry_run:
        filepath.write_text("\n".join(lines), encoding="utf-8")

    return changed


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    # Find all ko/ .py files (excluding tests)
    target_files = sorted(
        p
        for p in REPO_ROOT.rglob("*/ko/**/*.py")
        if "/tests/" not in str(p) and "__pycache__" not in str(p)
    )

    total_files = 0
    total_comments = 0
    modified_files = 0

    for filepath in target_files:
        total_files += 1
        count = process_file(filepath, dry_run=dry_run)
        if count > 0:
            modified_files += 1
            total_comments += count
            if dry_run:
                print(
                    f"  Would modify: {filepath.relative_to(REPO_ROOT)} ({count} comments)"
                )

    prefix = "[DRY RUN] " if dry_run else ""
    print(f"\n{prefix}Scanned: {total_files} files")
    print(f"{prefix}Modified: {modified_files} files")
    print(f"{prefix}Translated: {total_comments} comments")


if __name__ == "__main__":
    main()
