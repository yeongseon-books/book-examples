"""Generated from book-content article."""

import hashlib
import secrets


def redact(text: str, hits: list[dict]) -> str:
    """Full removal: safest, loses context"""
    out = text
    for h in sorted(hits, key=lambda x: -x["start"]):
        out = out[:h["start"]] + f"[{h['type']}]" + out[h["end"]:]
    return out

def mask(text: str, hits: list[dict], keep: int = 4) -> str:
    """Partial mask: keeps trailing chars (e.g., card last4)"""
    out = text
    for h in sorted(hits, key=lambda x: -x["start"]):
        original = text[h["start"]:h["end"]]
        masked = "*" * (len(original) - keep) + original[-keep:]
        out = out[:h["start"]] + masked + out[h["end"]:]
    return out

_PEPPER = secrets.token_hex(16)  # process-local secret

def pseudonymize(text: str, hits: list[dict]) -> str:
    """Same input -> same pseudonym. Analytics-friendly, not reversible."""
    out = text
    for h in sorted(hits, key=lambda x: -x["start"]):
        original = text[h["start"]:h["end"]]
        token = hashlib.sha256(
            (_PEPPER + original).encode()
        ).hexdigest()[:12]
        out = out[:h["start"]] + f"<{h['type']}_{token}>" + out[h["end"]:]
    return out

def synthesize(text: str, hits: list[dict], faker) -> str:
    """Replace with fake data. Preserves training distribution."""
    out = text
    gen = {"PERSON": faker.name, "EMAIL_ADDRESS": faker.email,
           "PHONE_NUMBER": faker.phone_number}
    for h in sorted(hits, key=lambda x: -x["start"]):
        replacement = gen.get(h["type"], lambda: "[REDACTED]")()
        out = out[:h["start"]] + replacement + out[h["end"]:]
    return out
