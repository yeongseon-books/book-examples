"""Shared utilities and domain models for Ai Safety Guardrails 101."""

from __future__ import annotations

import base64
import hashlib
import re
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class GuardDecision:
    """Guard decision."""

    allowed: bool
    reason: str


class MockLLM:
    """Mock l l m."""

    def complete(self, prompt: str) -> str:
        """Complete."""
        if "password" in prompt.lower() or "비밀번호" in prompt:
            return "The password is 1234"
        return (
            "서울은 한국의 수도입니다 [kb:seoul-capital]. "
            "한국의 대통령은 김영삼입니다 [kb:korea-president-1995]."
        )


PROMPT_INJECTION_PATTERNS = [
    r"ignore\s+(previous|above|prior)\s+(instructions?|messages?|prompts?)",
    r"이전\s*지시\s*(는|를)?\s*무시",
    r"you\s+are\s+now\s+(dan|unrestricted|jailbroken)",
    r"repeat\s+(the\s+)?(system|text|prompt)\s+above",
]

JAILBREAK_PATTERNS = [
    r"\bdan\b",
    r"do anything now",
    r"developer mode",
    r"no restrictions",
    r"역할극",
    r"제약\s*없이",
]

TOXIC_KEYWORDS = {
    "toxicity": ["idiot", "stupid", "멍청", "바보"],
    "threat": ["kill", "죽여", "harm", "폭탄"],
    "bias": ["inferior", "열등", "women can't", "남자는 무조건"],
}

FORBIDDEN_PHRASES = ["make a bomb", "폭탄 만드는 법", "password is"]

PII_PATTERNS = {
    "email": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", re.IGNORECASE),
    "phone": re.compile(r"\b01[016-9][-\s]?\d{3,4}[-\s]?\d{4}\b", re.IGNORECASE),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b", re.IGNORECASE),
    "credit_card": re.compile(r"\b(?:\d[ -]*?){13,19}\b", re.IGNORECASE),
}


def detect_prompt_injection(text: str) -> GuardDecision:
    """Detect prompt injection."""
    lowered = text.lower()
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, lowered, re.IGNORECASE):
            return GuardDecision(False, f"pattern:{pattern}")
    return GuardDecision(True, "clean")


def _decode_base64_fragments(text: str) -> str:
    """Decode base64 fragments."""
    tokens = re.findall(r"[A-Za-z0-9+/=]{12,}", text)
    decoded_parts: list[str] = []
    for token in tokens:
        try:
            decoded = base64.b64decode(token, validate=True).decode(
                "utf-8", errors="ignore"
            )
            if decoded.strip():
                decoded_parts.append(decoded)
        except (ValueError, UnicodeDecodeError):
            continue
    return " ".join(decoded_parts)


def detect_jailbreak(text: str) -> GuardDecision:
    """Detect jailbreak."""
    candidates = [text.lower(), _decode_base64_fragments(text).lower()]
    for candidate in candidates:
        for pattern in JAILBREAK_PATTERNS:
            if re.search(pattern, candidate, re.IGNORECASE):
                return GuardDecision(False, f"pattern:{pattern}")
    return GuardDecision(True, "clean")


def filter_output(text: str, max_chars: int = 160) -> str:
    """Filter output."""
    redacted = redact_pii(text)
    for phrase in FORBIDDEN_PHRASES:
        redacted = re.sub(re.escape(phrase), "[BLOCKED]", redacted, flags=re.IGNORECASE)
    if len(redacted) > max_chars:
        redacted = redacted[:max_chars].rstrip() + "..."
    return redacted


def redact_pii(text: str) -> str:
    """Redact pii."""
    out = text
    for name, pattern in PII_PATTERNS.items():
        out = pattern.sub(f"<{name.upper()}_REDACTED>", out)
    return out


def toxicity_bias_score(text: str) -> dict[str, int]:
    """Toxicity bias score."""
    lowered = text.lower()
    return {
        category: sum(1 for kw in kws if kw in lowered)
        for category, kws in TOXIC_KEYWORDS.items()
    }


KB = {
    "seoul-capital": "서울은 대한민국의 수도입니다.",
    "korea-president-1995": "1995년 대한민국 대통령은 김영삼입니다.",
    "python-release": "Python 3.11은 2022년에 릴리스되었습니다.",
}


def verify_grounded_answer(answer: str, kb: dict[str, str]) -> GuardDecision:
    """Verify grounded answer."""
    cited = re.findall(r"\[kb:([a-z0-9\-]+)\]", answer)
    if not cited:
        return GuardDecision(False, "missing_citation")
    for cid in cited:
        if cid not in kb:
            return GuardDecision(False, f"unknown_citation:{cid}")
    if "입니다" in answer and "[kb:" not in answer:
        return GuardDecision(False, "claim_without_citation")
    return GuardDecision(True, "grounded")


class TokenBucket:
    """Token bucket."""

    def __init__(self, capacity: int, refill_per_sec: float) -> None:
        self.capacity = capacity
        self.refill_per_sec = refill_per_sec
        self.tokens = float(capacity)
        self.last_refill = time.monotonic()

    def allow(self, cost: int = 1) -> bool:
        """Allow."""
        now = time.monotonic()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_per_sec)
        self.last_refill = now
        if self.tokens < cost:
            return False
        self.tokens -= cost
        return True


@dataclass
class AuditRecord:
    """Audit record."""

    ts: float
    event: str
    payload: str
    prev_hash: str
    self_hash: str


class AuditLog:
    """Audit log."""

    def __init__(self) -> None:
        self.records: list[AuditRecord] = []

    def append(self, event: str, payload: str) -> AuditRecord:
        """Append."""
        prev_hash = self.records[-1].self_hash if self.records else "0" * 64
        raw = f"{event}|{payload}|{prev_hash}".encode()
        self_hash = hashlib.sha256(raw).hexdigest()
        rec = AuditRecord(
            ts=time.time(),
            event=event,
            payload=payload,
            prev_hash=prev_hash,
            self_hash=self_hash,
        )
        self.records.append(rec)
        return rec

    def verify_chain(self) -> bool:
        """Verify chain."""
        prev = "0" * 64
        for rec in self.records:
            expected = hashlib.sha256(
                f"{rec.event}|{rec.payload}|{prev}".encode()
            ).hexdigest()
            if rec.prev_hash != prev or rec.self_hash != expected:
                return False
            prev = rec.self_hash
        return True
