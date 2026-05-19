import hashlib
import hmac
import html
import secrets

from common import assert_demo


def insecure_render(comment: str) -> str:
    return f"<p>{comment}</p>"


def safe_render(comment: str) -> str:
    return f"<p>{html.escape(comment)}</p>"


def make_csrf_token(session_id: str, key: bytes) -> str:
    nonce = secrets.token_hex(8)
    sig = hmac.new(key, f"{session_id}:{nonce}".encode(), hashlib.sha256).hexdigest()
    return f"{nonce}.{sig}"


def verify_csrf_token(session_id: str, token: str, key: bytes) -> bool:
    try:
        nonce, sig = token.split(".", 1)
    except ValueError:
        return False
    expected = hmac.new(
        key, f"{session_id}:{nonce}".encode(), hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(sig, expected)


def run_demo():
    payload = "<script>alert(1)</script>"
    insecure_detected = "<script>" in insecure_render(payload)
    key = b"demo-csrf-key"
    token = make_csrf_token("sid1", key)
    safe_ok = "<script>" not in safe_render(payload) and verify_csrf_token(
        "sid1", token, key
    )
    return assert_demo(insecure_detected, safe_ok)
