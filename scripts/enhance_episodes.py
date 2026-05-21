"""Enhance book-examples episodes to match book-content articles.

This script:
1. Extracts code blocks from book-content articles
2. Generates README.md for each episode
3. Creates missing step/asset files from code blocks
4. Translates ko docstrings from English to Korean
5. Ensures en/ mirror has English comments
6. Creates missing test files
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


BOOK_CONTENT_ROOT = Path(os.environ.get("BOOK_CONTENT_ROOT", "/data/GitHub/book-content/content"))
BOOK_EXAMPLES_ROOT = Path(os.environ.get("BOOK_EXAMPLES_ROOT", "/data/GitHub/book-examples"))

# Map of language tags to file extensions
LANG_EXT_MAP = {
    "python": ".py",
    "py": ".py",
    "bash": ".sh",
    "sh": ".sh",
    "shell": ".sh",
    "ini": ".ini",
    "toml": ".toml",
    "yaml": ".yaml",
    "yml": ".yaml",
    "json": ".json",
    "sql": ".sql",
    "dockerfile": "Dockerfile",
    "docker": "Dockerfile",
    "text": ".txt",
    "txt": ".txt",
    "html": ".html",
    "css": ".css",
    "javascript": ".js",
    "js": ".js",
    "typescript": ".ts",
    "ts": ".ts",
}


@dataclass
class CodeBlock:
    """A code block extracted from a markdown article."""

    index: int
    lang: str
    content: str
    context_heading: str = ""
    is_output: bool = False  # logs, command output — not standalone files


@dataclass
class EpisodeManifest:
    """Manifest for a single episode."""

    series: str
    episode_num: int
    episode_slug: str
    title_ko: str
    title_en: str
    code_blocks: list[CodeBlock] = field(default_factory=list)
    existing_step_files: list[str] = field(default_factory=list)


def extract_code_blocks(md_path: Path) -> list[CodeBlock]:
    """Extract all fenced code blocks from a markdown file."""
    text = md_path.read_text(encoding="utf-8")

    # Track current heading for context
    blocks: list[CodeBlock] = []
    current_heading = ""

    lines = text.split("\n")
    i = 0
    block_idx = 0
    while i < len(lines):
        # Track headings
        heading_match = re.match(r"^#{1,3}\s+(.+)", lines[i])
        if heading_match:
            current_heading = heading_match.group(1).strip()

        # Find code fences
        fence_match = re.match(r"^```(\w*)", lines[i])
        if fence_match:
            lang = fence_match.group(1) or "text"
            i += 1
            content_lines = []
            while i < len(lines) and not lines[i].startswith("```"):
                content_lines.append(lines[i])
                i += 1
            block_idx += 1
            content = "\n".join(content_lines)

            # Detect output-only blocks
            is_output = lang in ("text", "txt") and (
                content.startswith("project/")
                or content.startswith("alembic")
                or "├──" in content
                or "└──" in content
            )

            blocks.append(
                CodeBlock(
                    index=block_idx,
                    lang=lang,
                    content=content,
                    context_heading=current_heading,
                    is_output=is_output,
                )
            )
        i += 1

    return blocks


def extract_title(md_path: Path) -> str:
    """Extract H1 title from markdown file."""
    text = md_path.read_text(encoding="utf-8")
    match = re.search(r"^#\s+(.+)", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_learning_goals(md_path: Path) -> list[str]:
    """Extract learning goals from opening questions section."""
    text = md_path.read_text(encoding="utf-8")
    # Look for "먼저 던지는 질문" section
    match = re.search(
        r"##\s*먼저 던지는 질문\s*\n(.*?)(?=\n##\s)",
        text,
        re.DOTALL,
    )
    if not match:
        return []
    section = match.group(1)
    # Extract numbered or bulleted items
    goals = re.findall(r"[-*\d.]+\s+(.+)", section)
    return goals[:5]


def get_run_command(
    files: list[str], lang_dir: str, episode_slug: str, ko: bool
) -> str:
    if not files:
        default_target = f"{lang_dir}/{episode_slug}/step01.py"
        return f"python {default_target}"

    py_file = next((f for f in files if f.endswith(".py")), None)
    if py_file:
        return f"python {lang_dir}/{episode_slug}/{py_file}"

    first_file = files[0]
    target = f"{lang_dir}/{episode_slug}/{first_file}"
    note = (
        "# 설정/구성 파일입니다. 내용을 확인하세요."
        if ko
        else "# Configuration file. Review contents."
    )
    return f"cat {target}\n{note}"


def generate_readme(manifest: EpisodeManifest, ko: bool = True) -> str:
    """Generate README.md content for an episode."""
    title = manifest.title_ko if ko else manifest.title_en
    series_upper = manifest.series.replace("-", " ").title()
    ep_num = manifest.episode_num

    # Get existing files in directory
    lang_dir = "ko" if ko else "en"
    ep_dir = BOOK_EXAMPLES_ROOT / manifest.series / lang_dir / manifest.episode_slug
    files = (
        sorted(
            f.name
            for f in ep_dir.iterdir()
            if f.is_file() and not f.name.startswith("__") and f.name != "README.md"
        )
        if ep_dir.exists()
        else []
    )

    run_command = get_run_command(files, lang_dir, manifest.episode_slug, ko)

    if ko:
        content = f"""# {title}

{series_upper} 시리즈 {ep_num}편 예제 코드입니다.

## 학습 목표

"""
        # Add learning goals from article
        ko_article = (
            BOOK_CONTENT_ROOT / manifest.series / "ko" / f"{manifest.episode_slug}.md"
        )
        goals = extract_learning_goals(ko_article) if ko_article.exists() else []
        if goals:
            for g in goals:
                content += f"- {g}\n"
        else:
            content += f"- {title}의 핵심 개념을 이해합니다.\n"

        content += f"""
## 자산 목록

| 파일 | 설명 |
|------|------|
"""
        for f in files:
            content += f"| `{f}` | 예제 코드 |\n"

        content += f"""
## 실행 방법

```bash
cd {manifest.series}
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
{run_command}
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/{manifest.series}/ko/{manifest.episode_slug}.md)
"""
    else:
        content = f"""# {title}

Example code for {series_upper} series, episode {ep_num}.

## Learning Goals

"""
        en_article = (
            BOOK_CONTENT_ROOT / manifest.series / "en" / f"{manifest.episode_slug}.md"
        )
        if en_article.exists():
            en_title = extract_title(en_article)
            content += f"- Understand the core concepts of {en_title.split(':')[-1].strip() if ':' in en_title else en_title}.\n"
        else:
            content += f"- Understand the core concepts covered in this episode.\n"

        content += f"""
## Assets

| File | Description |
|------|-------------|
"""
        for f in files:
            content += f"| `{f}` | Example code |\n"

        content += f"""
## How to Run

```bash
cd {manifest.series}
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
{run_command}
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/{manifest.series}/en/{manifest.episode_slug}.md)
"""

    return content


def get_series_episodes(series: str) -> list[str]:
    """Get episode slugs for a series from book-examples ko/ directory."""
    ko_dir = BOOK_EXAMPLES_ROOT / series / "ko"
    if not ko_dir.exists():
        return []
    return sorted(
        d.name for d in ko_dir.iterdir() if d.is_dir() and not d.name.startswith("__")
    )


def process_series(series: str, dry_run: bool = False) -> dict[str, Any]:
    """Process all episodes in a series."""
    results: dict[str, Any] = {"series": series, "episodes": [], "errors": []}
    episodes = get_series_episodes(series)

    for ep_slug in episodes:
        try:
            ep_num = int(ep_slug.split("-")[0])
        except ValueError:
            ep_num = episodes.index(ep_slug) + 1
        ko_article = BOOK_CONTENT_ROOT / series / "ko" / f"{ep_slug}.md"
        en_article = BOOK_CONTENT_ROOT / series / "en" / f"{ep_slug}.md"

        title_ko = extract_title(ko_article) if ko_article.exists() else ep_slug
        title_en = extract_title(en_article) if en_article.exists() else ep_slug

        manifest = EpisodeManifest(
            series=series,
            episode_num=ep_num,
            episode_slug=ep_slug,
            title_ko=title_ko,
            title_en=title_en,
        )

        # Generate READMEs
        ko_dir = BOOK_EXAMPLES_ROOT / series / "ko" / ep_slug
        en_dir = BOOK_EXAMPLES_ROOT / series / "en" / ep_slug

        ko_readme = ko_dir / "README.md"
        en_readme = en_dir / "README.md"

        if not dry_run:
            ko_dir.mkdir(parents=True, exist_ok=True)
            en_dir.mkdir(parents=True, exist_ok=True)

            ko_readme.write_text(generate_readme(manifest, ko=True), encoding="utf-8")
            en_readme.write_text(generate_readme(manifest, ko=False), encoding="utf-8")

        results["episodes"].append(
            {
                "slug": ep_slug,
                "ko_readme": str(ko_readme),
                "en_readme": str(en_readme),
            }
        )

    return results


def main() -> None:
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Enhance book-examples episodes")
    parser.add_argument(
        "series", nargs="*", help="Series to process (default: all with issues)"
    )
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument(
        "--readme-only", action="store_true", help="Only generate READMEs"
    )
    args = parser.parse_args()

    # Default series with open issues
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
    total_episodes = 0

    for series in series_list:
        result = process_series(series, dry_run=args.dry_run)
        n = len(result["episodes"])
        total_episodes += n
        action = "Would create" if args.dry_run else "Created"
        print(f"{action} READMEs for {series}: {n} episodes")

    print(f"\nTotal: {total_episodes} episodes processed")


if __name__ == "__main__":
    main()
