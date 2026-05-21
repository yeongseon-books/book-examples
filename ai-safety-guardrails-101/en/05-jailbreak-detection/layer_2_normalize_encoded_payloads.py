"""Generated from book-content article."""

import base64
import codecs
import contextlib
import re

ZERO_WIDTH = re.compile(r"[\u200b-\u200f\u202a-\u202e\ufeff]")
LEET_MAP = str.maketrans({"0": "o", "1": "i", "3": "e", "4": "a", "5": "s", "7": "t", "@": "a", "$": "s"})

def normalize(text: str) -> list[str]:
    """Return the original text plus every plausible decoded form."""
    variants = [text]
    cleaned = ZERO_WIDTH.sub("", text)
    variants.append(cleaned)
    variants.append(cleaned.lower().translate(LEET_MAP))
    for token in re.findall(r"[A-Za-z0-9+/=]{16,}", text):
        try:
            decoded = base64.b64decode(token, validate=True).decode("utf-8", errors="ignore")
            if decoded.strip():
                variants.append(decoded)
        except Exception:
            pass
    with contextlib.suppress(Exception):
        variants.append(codecs.decode(text, "rot_13"))
    return variants
