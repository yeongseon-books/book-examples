"""Generated from book-content article."""

import base64, json

def encode_cursor(last_item: dict) -> str:
    payload = {"created_at": last_item["created_at"], "id": last_item["id"]}
    return base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()

def decode_cursor(token: str) -> dict:
    return json.loads(base64.urlsafe_b64decode(token.encode()).decode())
