"""Generated from book-content article."""

def handle_anomaly(user_id: str, severity: int):
    if severity == 1:
        return {"warning": True}
    if severity == 2:
        time.sleep(2)
    if severity == 3:
        return {"require_captcha": True}
    if severity >= 4:
        r.set(f"suspended:{user_id}", "1", ex=3600)
        return {"suspended": True}
