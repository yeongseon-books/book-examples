"""Materialize file-like code blocks from book-content articles into book-examples.

Rules:
- Python blocks with a '# filename.py' header → create that file
- Python blocks without header → create step{NN}_{context}.py
- Config blocks (ini, yaml, toml, json) → create with appropriate filename
- Dockerfile blocks → create as Dockerfile
- Bash blocks → skip (commands, not files)
- Text blocks with tree/log output → skip (not files)
- HTML/CSS/JS blocks → create with appropriate extension

Existing step*.py files are preserved. New assets are added alongside them.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any
import os


BOOK_CONTENT_ROOT = Path(os.environ.get("BOOK_CONTENT_ROOT", "/data/GitHub/book-content/content"))
BOOK_EXAMPLES_ROOT = Path(os.environ.get("BOOK_EXAMPLES_ROOT", "/data/GitHub/book-examples"))

# Languages that represent standalone files
FILE_LANGS = {
    "python",
    "py",
    "ini",
    "yaml",
    "yml",
    "toml",
    "json",
    "dockerfile",
    "docker",
    "html",
    "css",
    "javascript",
    "js",
    "typescript",
    "ts",
    "sql",
}

# Languages to skip (commands, not files)
SKIP_LANGS = {"bash", "sh", "shell", "text", "txt", "console", ""}

LANG_EXT = {
    "python": ".py",
    "py": ".py",
    "ini": ".ini",
    "toml": ".toml",
    "yaml": ".yaml",
    "yml": ".yaml",
    "json": ".json",
    "sql": ".sql",
    "html": ".html",
    "css": ".css",
    "javascript": ".js",
    "js": ".js",
    "typescript": ".ts",
    "ts": ".ts",
    "dockerfile": "",
    "docker": "",
}


def slugify(text: str) -> str:
    """Convert text to a slug suitable for filenames."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = text.strip("_")
    return text[:40] if text else "snippet"


def extract_filename_from_content(content: str, lang: str) -> str | None:
    """Try to extract a filename from the first line comment."""
    first_line = content.split("\n")[0].strip()

    # Pattern: # filename.ext or // filename.ext
    patterns = [
        r"^#\s*([\w./+-]+\.\w+)",  # Python/shell style
        r"^//\s*([\w./+-]+\.\w+)",  # JS/TS style
        r"^/\*\s*([\w./+-]+\.\w+)",  # CSS style
        r"^<!--\s*([\w./+-]+\.\w+)",  # HTML style
    ]
    for pat in patterns:
        m = re.match(pat, first_line)
        if m:
            # Return just the basename
            return Path(m.group(1)).name

    # For Dockerfile
    if lang in ("dockerfile", "docker"):
        return "Dockerfile"

    return None


def should_materialize(lang: str, content: str) -> bool:
    """Decide if a code block should become a file."""
    if lang in SKIP_LANGS:
        return False
    if lang not in FILE_LANGS:
        return False

    # Skip very short snippets (< 3 lines of actual code)
    lines = [l for l in content.strip().split("\n") if l.strip()]
    if len(lines) < 3:
        return False

    # Skip output-like content in any language
    if "├──" in content or "└──" in content:
        return False

    return True


def extract_blocks_from_article(md_path: Path) -> list[dict[str, Any]]:
    """Extract materializable code blocks from a markdown file."""
    text = md_path.read_text(encoding="utf-8")
    blocks = []
    current_heading = ""

    lines = text.split("\n")
    i = 0
    block_idx = 0

    while i < len(lines):
        # Track headings for context
        heading_match = re.match(r"^#{1,3}\s+(.+)", lines[i])
        if heading_match:
            current_heading = heading_match.group(1).strip()

        fence_match = re.match(r"^```(\w*)", lines[i])
        if fence_match:
            lang = fence_match.group(1) or ""
            i += 1
            content_lines = []
            while i < len(lines) and not lines[i].startswith("```"):
                content_lines.append(lines[i])
                i += 1
            block_idx += 1
            content = "\n".join(content_lines)

            if should_materialize(lang, content):
                filename = extract_filename_from_content(content, lang)
                if not filename:
                    # Generate filename from context
                    ext = LANG_EXT.get(lang, ".txt")
                    context_slug = (
                        slugify(current_heading)
                        if current_heading
                        else f"block{block_idx:02d}"
                    )
                    filename = f"{context_slug}{ext}"

                blocks.append(
                    {
                        "index": block_idx,
                        "lang": lang,
                        "content": content,
                        "filename": filename,
                        "heading": current_heading,
                    }
                )
        i += 1

    return blocks


def materialize_episode(series: str, ep_slug: str, lang_dir: str = "ko") -> list[str]:
    """Materialize code blocks for one episode. Returns list of created files."""
    article_path = BOOK_CONTENT_ROOT / series / lang_dir / f"{ep_slug}.md"
    if not article_path.exists():
        return []

    target_dir = BOOK_EXAMPLES_ROOT / series / lang_dir / ep_slug
    target_dir.mkdir(parents=True, exist_ok=True)

    blocks = extract_blocks_from_article(article_path)
    created = []

    # Track filenames to avoid duplicates
    used_names: set[str] = set()
    # Existing files should not be overwritten
    existing = {f.name for f in target_dir.iterdir() if f.is_file()}

    for block in blocks:
        filename = block["filename"]

        # Avoid overwriting existing files
        if filename in existing:
            continue

        # Avoid duplicates in this batch
        if filename in used_names:
            base, ext = filename.rsplit(".", 1) if "." in filename else (filename, "")
            filename = (
                f"{base}_{block['index']:02d}.{ext}"
                if ext
                else f"{base}_{block['index']:02d}"
            )
        used_names.add(filename)

        # Write the file
        filepath = target_dir / filename
        content = block["content"]

        # Add docstring header for Python files
        if (
            filename.endswith(".py")
            and not content.startswith('"""')
            and not content.startswith("#!")
        ):
            # Don't add if first line is a comment with filename
            if content.startswith("# "):
                pass  # keep as-is
            else:
                header = f'"""Generated from book-content article."""\n\n'
                content = header + content

        filepath.write_text(content + "\n", encoding="utf-8")
        created.append(filename)

    return created


def process_series(series: str, dry_run: bool = False) -> dict[str, Any]:
    """Process all episodes in a series."""
    results = {"series": series, "total_created": 0, "episodes": {}}

    ko_dir = BOOK_EXAMPLES_ROOT / series / "ko"
    if not ko_dir.exists():
        return results

    episodes = sorted(
        d.name for d in ko_dir.iterdir() if d.is_dir() and not d.name.startswith("__")
    )

    for ep_slug in episodes:
        if dry_run:
            # Just count blocks
            article = BOOK_CONTENT_ROOT / series / "ko" / f"{ep_slug}.md"
            if article.exists():
                blocks = extract_blocks_from_article(article)
                results["episodes"][ep_slug] = len(blocks)
                results["total_created"] += len(blocks)
        else:
            # Materialize for ko and en
            ko_created = materialize_episode(series, ep_slug, "ko")
            en_created = materialize_episode(series, ep_slug, "en")
            total = len(ko_created) + len(en_created)
            if total:
                results["episodes"][ep_slug] = {"ko": ko_created, "en": en_created}
            results["total_created"] += total

    return results


def main() -> None:
    """Main entry."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Materialize code blocks from articles"
    )
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
    grand_total = 0

    for series in series_list:
        result = process_series(series, dry_run=args.dry_run)
        n = result["total_created"]
        grand_total += n
        if n:
            action = "Would create" if args.dry_run else "Created"
            print(f"{action} {n} files for {series}")

    print(
        f"\nTotal: {grand_total} files {'would be created' if args.dry_run else 'created'}"
    )


if __name__ == "__main__":
    main()
