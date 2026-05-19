"""Shared utilities and domain models for Information Security 101."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import re
import secrets
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


def risk_score(likelihood: int, impact: int) -> int:
    """Risk score."""
    return likelihood * impact


class PasswordHasher:
    """Password hasher."""

    def hash_password_pbkdf2(self, password: str) -> str:
        """Hash password pbkdf2."""
        salt = secrets.token_bytes(16)
        digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
        return "pbkdf2$" + base64.b64encode(salt + digest).decode()

    def hash_password_scrypt(self, password: str) -> str:
        """Hash password scrypt."""
        salt = secrets.token_bytes(16)
        digest = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1)
        return "scrypt$" + base64.b64encode(salt + digest).decode()

    def verify(self, password: str, encoded: str) -> bool:
        """Verify."""
        scheme, payload = encoded.split("$", 1)
        raw = base64.b64decode(payload.encode())
        salt, expected = raw[:16], raw[16:]
        if scheme == "pbkdf2":
            actual = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
        elif scheme == "scrypt":
            actual = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1)
        else:
            raise ValueError("unknown scheme")
        return hmac.compare_digest(actual, expected)


class AuthSystem:
    """Auth system."""

    def __init__(self, hasher: PasswordHasher | None = None) -> None:
        self.hasher = hasher or PasswordHasher()
        self.users: dict[str, tuple[str, str]] = {}
        self.role_perms = {"admin": {"read", "write", "delete"}, "user": {"read"}}

    def register(self, username: str, password: str, role: str) -> None:
        """Register."""
        self.users[username] = (self.hasher.hash_password_pbkdf2(password), role)

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate."""
        user = self.users.get(username)
        if not user:
            return False
        return self.hasher.verify(password, user[0])

    def authorize(self, username: str, action: str) -> bool:
        """Authorize."""
        user = self.users.get(username)
        if not user:
            return False
        role = user[1]
        return action in self.role_perms.get(role, set())


class SymmetricCipher:
    """Symmetric cipher."""

    def __init__(self, key: bytes) -> None:
        self.key = key

    def _keystream(self, nonce: bytes, length: int) -> bytes:
        """Keystream."""
        out = bytearray()
        counter = 0
        while len(out) < length:
            block = hashlib.sha256(
                self.key + nonce + counter.to_bytes(4, "big")
            ).digest()
            out.extend(block)
            counter += 1
        return bytes(out[:length])

    def encrypt(self, plaintext: bytes) -> str:
        """Encrypt."""
        nonce = secrets.token_bytes(12)
        ks = self._keystream(nonce, len(plaintext))
        ciphertext = bytes(a ^ b for a, b in zip(plaintext, ks, strict=False))
        mac = hmac.new(self.key, nonce + ciphertext, hashlib.sha256).digest()
        return base64.urlsafe_b64encode(nonce + ciphertext + mac).decode()

    def decrypt(self, token: str) -> bytes:
        """Decrypt."""
        raw = base64.urlsafe_b64decode(token.encode())
        nonce, rest = raw[:12], raw[12:]
        ciphertext, mac = rest[:-32], rest[-32:]
        expected = hmac.new(self.key, nonce + ciphertext, hashlib.sha256).digest()
        if not hmac.compare_digest(mac, expected):
            raise ValueError("tampered token")
        ks = self._keystream(nonce, len(ciphertext))
        return bytes(a ^ b for a, b in zip(ciphertext, ks, strict=False))


class TLSCertParser:
    """TLS cert parser."""

    def parse_pem_text(self, pem_text: str) -> dict[str, Any]:
        """Parse pem text."""
        return {
            "has_begin": "-----BEGIN CERTIFICATE-----" in pem_text,
            "has_end": "-----END CERTIFICATE-----" in pem_text,
            "line_count": len([line for line in pem_text.splitlines() if line.strip()]),
        }


class WebRequestSanitizer:
    """Web request sanitizer."""

    def validate_headers(self, headers: dict[str, str]) -> bool:
        """Validate headers."""
        host = headers.get("Host", "")
        return bool(host) and "\n" not in host and "\r" not in host

    def check_csrf(self, headers: dict[str, str], session_token: str) -> bool:
        """Check csrf."""
        return hmac.compare_digest(headers.get("X-CSRF", ""), session_token)

    def cors_allows(self, origin: str, allowlist: set[str]) -> bool:
        """Cors allows."""
        return origin in allowlist


class SQLInjectionDetector:
    """SQL injection detector."""

    PATTERNS = [r"'\s*or\s+1=1", r"union\s+select", r"--", r";\s*drop\s+table"]

    def is_suspicious(self, text: str) -> bool:
        """Is suspicious."""
        low = text.lower()
        return any(re.search(pattern, low) for pattern in self.PATTERNS)


class XSSDetector:
    """XSS detector."""

    PATTERNS = [r"<script", r"onerror\s*=", r"javascript:"]

    def is_suspicious(self, text: str) -> bool:
        """Is suspicious."""
        low = text.lower()
        return any(re.search(pattern, low) for pattern in self.PATTERNS)


class SecretsVault:
    """Secrets vault."""

    def __init__(self, master_key: bytes) -> None:
        self.cipher = SymmetricCipher(master_key)
        self.data: dict[str, str] = {}
        self.audit: list[str] = []

    def put(self, key: str, value: str) -> None:
        """Put."""
        self.data[key] = self.cipher.encrypt(value.encode())
        self.audit.append(f"put:{key}")

    def get(self, key: str) -> str:
        """Get."""
        self.audit.append(f"get:{key}")
        return self.cipher.decrypt(self.data[key]).decode()

    def rotate_master_key(self, new_key: bytes) -> None:
        """Rotate master key."""
        old = self.cipher
        new_cipher = SymmetricCipher(new_key)
        for key, token in list(self.data.items()):
            plain = old.decrypt(token)
            self.data[key] = new_cipher.encrypt(plain)
        self.cipher = new_cipher
        self.audit.append("rotate")


class LeastPrivilegeChecker:
    """Least privilege checker."""

    def __init__(self, policy: dict[str, dict[str, set[str]]]) -> None:
        self.policy = policy

    def allow(self, role: str, action: str, resource: str) -> bool:
        """Allow."""
        return action in self.policy.get(role, {}).get(resource, set())


@dataclass
class AuditRecord:
    """Audit record."""

    ts: str
    event: dict[str, Any]
    mac: str


class AuditLogger:
    """Audit logger."""

    def __init__(self, key: bytes) -> None:
        self.key = key
        self.records: list[AuditRecord] = []

    def _payload(self, event: dict[str, Any]) -> bytes:
        """Payload."""
        return json.dumps(event, sort_keys=True, separators=(",", ":")).encode()

    def append(self, event: dict[str, Any]) -> AuditRecord:
        """Append."""
        prev_mac = self.records[-1].mac.encode() if self.records else b"genesis"
        payload = self._payload(event)
        mac = hmac.new(self.key, prev_mac + payload, hashlib.sha256).hexdigest()
        rec = AuditRecord(datetime.now(timezone.utc).isoformat(), event, mac)
        self.records.append(rec)
        return rec

    def verify_chain(self) -> bool:
        """Verify chain."""
        prev_mac = b"genesis"
        for rec in self.records:
            payload = self._payload(rec.event)
            expected = hmac.new(
                self.key, prev_mac + payload, hashlib.sha256
            ).hexdigest()
            if not hmac.compare_digest(expected, rec.mac):
                return False
            prev_mac = rec.mac.encode()
        return True


class IncidentDetector:
    """Incident detector."""

    def detect_bruteforce(
        self, events: list[dict[str, Any]], threshold: int = 5
    ) -> bool:
        """Detect bruteforce."""
        failures = [e for e in events if e.get("event") == "auth" and not e.get("ok")]
        return len(failures) >= threshold

    def detect_impossible_travel(
        self, events: list[dict[str, Any]], max_km_per_h: int = 900
    ) -> bool:
        """Detect impossible travel."""
        by_user: dict[str, list[dict[str, Any]]] = {}
        for e in events:
            by_user.setdefault(str(e.get("user", "")), []).append(e)
        for _, user_events in by_user.items():
            user_events.sort(key=lambda x: x.get("ts", 0))
            for first, second in zip(user_events, user_events[1:], strict=False):
                dt_h = max((second["ts"] - first["ts"]) / 3600.0, 1e-6)
                speed = abs(second.get("km", 0) - first.get("km", 0)) / dt_h
                if speed > max_km_per_h:
                    return True
        return False
