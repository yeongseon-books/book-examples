from common import has_star_bullet, parse_markdown_sections


REQUIRED = ["Summary", "Experience", "Skills", "Projects", "Education"]


def validate_resume(markdown: str) -> dict:
    sections = parse_markdown_sections(markdown)
    missing = [s for s in REQUIRED if s not in sections]
    experience_lines = sections.get("Experience", "").splitlines()
    star_bullets = [ln for ln in experience_lines if has_star_bullet(ln)]
    score = max(0, 100 - len(missing) * 15 + len(star_bullets) * 5)
    return {"missing": missing, "star_bullets": star_bullets, "score": score}
