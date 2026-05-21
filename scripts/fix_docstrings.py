"""Fix ko/ docstrings to Korean and en/ to English.

Scans all step*.py in ko/ directories and rewrites module docstrings
and function docstrings to Korean. Does the same for en/ to ensure English.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

BOOK_EXAMPLES_ROOT = Path(os.environ.get("BOOK_EXAMPLES_ROOT", "/data/GitHub/book-examples"))

# Korean docstring templates based on common patterns
KO_MODULE_TEMPLATE = '"""{series_name} - {ep_num}편: {ep_title} 예제."""'
EN_MODULE_TEMPLATE = '"""{series_name} - Episode {ep_num}: {ep_title} example."""'

# Common function docstring translations
FUNC_DOC_MAP_KO = {
    "Run demo.": "데모를 실행합니다.",
    "Run init demo.": "초기화 데모를 실행합니다.",
    "Run demo": "데모를 실행합니다.",
    "Main entry point.": "메인 진입점입니다.",
    "Run main demo.": "메인 데모를 실행합니다.",
}

FUNC_DOC_MAP_EN = {v: k for k, v in FUNC_DOC_MAP_KO.items()}


def series_display_name(series_id: str) -> str:
    """Convert series-id to display name."""
    return series_id.replace("-", " ").replace("101", "101").title()


def ep_title_from_slug(slug: str) -> str:
    """Extract episode title from slug: 01-why-alembic-and-init -> why alembic and init."""
    parts = slug.split("-", 1)
    return parts[1].replace("-", " ") if len(parts) > 1 else slug


def fix_docstrings(
    file_path: Path, to_korean: bool, series: str, ep_slug: str, ep_num: int
) -> bool:
    """Fix docstrings in a Python file. Returns True if modified."""
    content = file_path.read_text(encoding="utf-8")
    original = content

    series_name = series_display_name(series)
    ep_title = ep_title_from_slug(ep_slug)

    # Fix module docstring (first triple-quoted string)
    if to_korean:
        new_module_doc = f'"""{series_name} - {ep_num}편: {ep_title} 예제."""'
    else:
        new_module_doc = f'"""{series_name} - Episode {ep_num}: {ep_title} example."""'

    # Replace first docstring
    content = re.sub(
        r'^""".*?"""',
        new_module_doc,
        content,
        count=1,
        flags=re.DOTALL,
    )

    # Fix function docstrings

    def replace_func_doc(match: re.Match) -> str:
        indent = match.group(1)
        doc = match.group(2)
        for en_doc, ko_doc in FUNC_DOC_MAP_KO.items():
            if to_korean and doc.strip() == en_doc:
                return f'{indent}"""{ko_doc}"""'
            elif not to_korean and doc.strip() == ko_doc:
                return f'{indent}"""{en_doc}"""'
        # Generic translation for unmatched
        if to_korean and not any(ord(c) > 127 for c in doc):
            # Simple pattern: "Verb noun." -> Korean equivalent
            return f'{indent}"""{doc}"""'  # keep as-is if no match
        return match.group(0)

    content = re.sub(
        r'([ \t]+)"""(.*?)"""',
        replace_func_doc,
        content,
    )

    # Add/fix inline comments
    if to_korean:
        # Remove English-only marker comments
        content = content.replace("# English mirror\n", "")
    else:
        # Ensure en files have English marker if they don't differ from ko
        pass

    if content != original:
        file_path.write_text(content, encoding="utf-8")
        return True
    return False


def process_series(series: str, dry_run: bool = False) -> dict[str, int]:
    """Process all episodes in a series."""
    ko_modified = 0
    en_modified = 0

    ko_dir = BOOK_EXAMPLES_ROOT / series / "ko"
    en_dir = BOOK_EXAMPLES_ROOT / series / "en"

    if not ko_dir.exists():
        return {"ko": 0, "en": 0}

    for ep_dir in sorted(ko_dir.iterdir()):
        if not ep_dir.is_dir() or ep_dir.name.startswith("__"):
            continue

        ep_slug = ep_dir.name
        ep_num = int(ep_slug.split("-")[0])

        # Fix ko files
        for py_file in sorted(ep_dir.glob("*.py")):
            if not dry_run:
                if fix_docstrings(
                    py_file,
                    to_korean=True,
                    series=series,
                    ep_slug=ep_slug,
                    ep_num=ep_num,
                ):
                    ko_modified += 1

        # Fix en files
        en_ep_dir = en_dir / ep_slug
        if en_ep_dir.exists():
            for py_file in sorted(en_ep_dir.glob("*.py")):
                if not dry_run:
                    if fix_docstrings(
                        py_file,
                        to_korean=False,
                        series=series,
                        ep_slug=ep_slug,
                        ep_num=ep_num,
                    ):
                        en_modified += 1

    return {"ko": ko_modified, "en": en_modified}


def main() -> None:
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Fix docstrings in ko/en files")
    parser.add_argument("series", nargs="*")
    parser.add_argument("--dry-run", action="store_true")
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
    total_ko = 0
    total_en = 0

    for series in series_list:
        result = process_series(series, dry_run=args.dry_run)
        total_ko += result["ko"]
        total_en += result["en"]
        if result["ko"] or result["en"]:
            print(f"{series}: ko={result['ko']}, en={result['en']} files modified")

    print(f"\nTotal: {total_ko} ko files, {total_en} en files modified")


if __name__ == "__main__":
    main()
