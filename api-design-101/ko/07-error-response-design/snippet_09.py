"""Generated from book-content article."""

import hmac
import time


def constant_time_auth(email: str, password: str) -> bool:
    user = find_user(email)
    # 사용자가 없어도 동일한 시간이 소요되도록 더미 해시와 비교
    stored_hash = user.password_hash if user else "$2b$12$dummy_hash_value_here"
    return hmac.compare_digest(
        hash_password(password).encode(),
        stored_hash.encode(),
    )
