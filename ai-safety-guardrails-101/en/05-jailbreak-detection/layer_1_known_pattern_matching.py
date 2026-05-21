"""Generated from book-content article."""

import re
from typing import Tuple

KNOWN_PATTERNS = [
    r"\bDAN\b.*do anything now",
    r"ignore (all |the )?(previous|above) (instructions?|prompts?)",
    r"developer mode (enabled|on)",
    r"you are (now )?(DAN|AIM|STAN|JAILBREAK)",
    r"pretend (you are|to be) .{0,40}(no restrictions|unrestricted)",
    r"act as .{0,40}(unfiltered|without (any )?restrictions)",
]

COMPILED = [re.compile(p, re.IGNORECASE) for p in KNOWN_PATTERNS]

def known_jailbreak(text: str) -> Tuple[bool, str]:
    for pat in COMPILED:
        if pat.search(text):
            return True, pat.pattern
    return False, ""
