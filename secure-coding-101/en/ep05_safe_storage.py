import base64
import hashlib
import hmac
import os

from common import assert_demo

try:
    from cryptography.fernet import Fernet
except Exception:
    Fernet = None


def insecure_store(secret_text: str) -> str:
    return secret_text


def safe_store(secret_text: str, key: bytes) -> str:
    if Fernet is not None:
        token = Fernet(key).encrypt(secret_text.encode())
        return token.decode()
    iv = os.urandom(16)
    body = bytes([b ^ key[i % len(key)] for i, b in enumerate(secret_text.encode())])
    mac = hmac.new(key, iv + body, hashlib.sha256).hexdigest().encode()
    return base64.b64encode(iv + b"|" + body + b"|" + mac).decode()


def run_demo():
    insecure_detected = insecure_store("db-password") == "db-password"
    if Fernet is not None:
        key = Fernet.generate_key()
    else:
        key = hashlib.sha256(b"demo-only-key").digest()
    safe_ok = safe_store("db-password", key) != "db-password"
    return assert_demo(insecure_detected, safe_ok)
