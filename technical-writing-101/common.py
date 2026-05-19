from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def _words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z']+", text)


def _sentences(text: str) -> list[str]:
    return [s for s in re.split(r"[.!?]+", text) if s.strip()]


def ep01_readability(text: str, lang: str = "en") -> dict:
    if lang == "en":
        words = _words(text)
        sents = _sentences(text)
        syllables = (
            sum(max(1, len(re.findall(r"[aeiouyAEIOUY]+", w))) for w in words) or 1
        )
        w_count = len(words) or 1
        s_count = len(sents) or 1
        score = 206.835 - 1.015 * (w_count / s_count) - 84.6 * (syllables / w_count)
        return {
            "language": "en",
            "flesch_like": round(score, 2),
            "words": w_count,
            "sentences": s_count,
        }
    chars = len(re.sub(r"\s+", "", text)) or 1
    s_count = len(_sentences(text)) or 1
    return {
        "language": "ko",
        "char_per_sentence": round(chars / s_count, 2),
        "sentences": s_count,
    }


def ep02_audience_profile(text: str) -> dict:
    depth_keywords = [
        "architecture",
        "latency",
        "throughput",
        "consistency",
        "trade-off",
        "complexity",
    ]
    jargon = [
        "idempotency",
        "serialization",
        "concurrency",
        "backpressure",
        "eventual",
        "invariant",
    ]
    lower = text.lower()
    depth_hits = sum(lower.count(k) for k in depth_keywords)
    jargon_hits = sum(lower.count(k) for k in jargon)
    words = len(_words(text)) or 1
    return {
        "depth_hits": depth_hits,
        "jargon_density": round(jargon_hits / words, 4),
        "audience": "advanced" if depth_hits >= 3 or jargon_hits >= 3 else "general",
    }


def _heading_levels(text: str) -> list[int]:
    levels = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+", line)
        if m:
            levels.append(len(m.group(1)))
    return levels


def ep03_structure_lint(text: str) -> dict:
    lines = text.splitlines()
    has_h1 = any(re.match(r"^#\s+", line) for line in lines)
    levels = _heading_levels(text)
    skipped = False
    for prev, cur in zip(levels, levels[1:]):
        if cur > prev + 1:
            skipped = True
            break
    return {
        "has_h1": has_h1,
        "heading_levels": levels,
        "no_skipped_levels": not skipped,
    }


def ep04_what_before_how(text: str) -> dict:
    headings = [
        re.sub(r"^#{1,6}\s+", "", ln).strip().lower()
        for ln in text.splitlines()
        if re.match(r"^#{1,6}\s+", ln)
    ]
    what_idx = next(
        (
            i
            for i, h in enumerate(headings)
            if "what" in h or "개요" in h or "정의" in h
        ),
        -1,
    )
    how_idx = next(
        (i for i, h in enumerate(headings) if "how" in h or "구현" in h or "방법" in h),
        -1,
    )
    ok = not (what_idx != -1 and how_idx != -1 and what_idx > how_idx)
    return {"what_index": what_idx, "how_index": how_idx, "what_before_how": ok}


def _code_blocks(lines: list[str]) -> list[tuple[int, int, str]]:
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r"^```(.*)$", lines[i])
        if not m:
            i += 1
            continue
        lang = m.group(1).strip()
        start = i
        i += 1
        while i < len(lines) and not lines[i].startswith("```"):
            i += 1
        end = i if i < len(lines) else len(lines) - 1
        out.append((start, end, lang))
        i += 1
    return out


def ep05_code_example_lint(text: str) -> dict:
    lines = text.splitlines()
    blocks = _code_blocks(lines)
    missing_lang = 0
    long_lines = 0
    explanation_ok = 0
    for start, end, lang in blocks:
        if not lang:
            missing_lang += 1
        for line in lines[start + 1 : end]:
            if len(line) > 100:
                long_lines += 1
        prev_line = lines[start - 1].strip() if start - 1 >= 0 else ""
        next_line = lines[end + 1].strip() if end + 1 < len(lines) else ""
        if (
            prev_line
            and not prev_line.startswith("#")
            and not prev_line.startswith("```")
        ) or (
            next_line
            and not next_line.startswith("#")
            and not next_line.startswith("```")
        ):
            explanation_ok += 1
    return {
        "code_blocks": len(blocks),
        "missing_language_tags": missing_lang,
        "long_code_lines": long_lines,
        "explained_blocks": explanation_ok,
    }


class _ImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.img_missing_alt = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "img":
            return
        attr = {k: v for k, v in attrs}
        if not attr.get("alt"):
            self.img_missing_alt += 1


def ep06_figure_table_lint(text: str) -> dict:
    parser = _ImageParser()
    parser.feed(text)
    md_img_missing_alt = sum(
        1 for m in re.finditer(r"!\[(.*?)\]\((.*?)\)", text) if not m.group(1).strip()
    )
    tables = [
        i
        for i, ln in enumerate(text.splitlines())
        if "|" in ln and re.search(r"\|", ln)
    ]
    caption_lines = [
        i
        for i, ln in enumerate(text.splitlines())
        if ln.strip().lower().startswith(("table:", "표:"))
    ]
    has_table = len(tables) > 0
    table_caption_ok = (not has_table) or bool(caption_lines)
    return {
        "images_missing_alt": parser.img_missing_alt + md_img_missing_alt,
        "has_table": has_table,
        "table_caption_ok": table_caption_ok,
    }


def ep07_readme_score(text: str) -> dict:
    required = ["install", "usage", "license"]
    lower = text.lower()
    present = [r for r in required if r in lower]
    badges = len(re.findall(r"\[!\[[^\]]+\]\([^\)]+\)\]\([^\)]+\)", text))
    return {
        "required_present": present,
        "required_score": len(present) / len(required),
        "badge_count": badges,
    }


def ep08_tutorial_structure(text: str) -> dict:
    has_prereq = bool(re.search(r"^##\s+(Prerequisites|사전 준비)", text, flags=re.M))
    has_outcome = bool(
        re.search(r"^##\s+(Expected Outcome|결과|Outcome)", text, flags=re.M)
    )
    steps = re.findall(r"^\d+\.\s+", text, flags=re.M)
    return {
        "has_prerequisites": has_prereq,
        "has_expected_outcome": has_outcome,
        "step_count": len(steps),
    }


def ep09_blog_vs_docs(text: str) -> dict:
    lower = text.lower()
    first_person = len(re.findall(r"\b(i|we|my|our)\b", lower))
    words = len(_words(text)) or 1
    headings = len(_heading_levels(text))
    code_blocks = len(_code_blocks(text.splitlines()))
    mode = "blog" if first_person >= 3 and code_blocks <= 1 else "docs"
    return {
        "first_person_count": first_person,
        "code_block_density": round(code_blocks / max(1, words / 1000), 3),
        "headings_per_1000_words": round(headings / max(1, words / 1000), 3),
        "classification": mode,
    }


def ep10_prepublish(text: str) -> dict:
    r3 = ep03_structure_lint(text)
    r5 = ep05_code_example_lint(text)
    r6 = ep06_figure_table_lint(text)
    r7 = ep07_readme_score(text)
    checks = {
        "ep03": r3["has_h1"] and r3["no_skipped_levels"],
        "ep05": r5["missing_language_tags"] == 0 and r5["long_code_lines"] == 0,
        "ep06": r6["images_missing_alt"] == 0 and r6["table_caption_ok"],
        "ep07": r7["required_score"] == 1.0,
    }
    return {"checks": checks, "pass": all(checks.values())}
