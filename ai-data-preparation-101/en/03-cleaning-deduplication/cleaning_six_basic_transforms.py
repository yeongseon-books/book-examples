"""Generated from book-content article."""

import re
import unicodedata
from html import unescape


def clean_text(text: str) -> str:
    if not text:
        return ""
    # 1. Encoding normalization (NFC: combine Hangul jamo)
    text = unicodedata.normalize("NFC", text)
    # 2. HTML entity decode
    text = unescape(text)
    # 3. HTML tag removal
    text = re.sub(r"<[^>]+>", " ", text)
    # 4. Control characters (keep tab/newline)
    text = "".join(ch for ch in text if ch == "\n" or ch == "\t" or ord(ch) >= 32)
    # 5. Collapse runs of whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # 6. Strip
    return text.strip()

# Test
samples = [
    "<p>Hello&nbsp;<b>world</b>!</p>",
    "Hello\u200b\u200bworld",  # zero-width space
    "Multi   spaces\n\n\n\nlines",
]
for s in samples:
    print(repr(clean_text(s)))
