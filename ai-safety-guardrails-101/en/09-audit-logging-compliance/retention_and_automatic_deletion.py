"""Generated from book-content article."""

from datetime import timedelta

RETENTION = {
    "audit_log": timedelta(days=365 * 7),     # 7 years
    "pii_store": timedelta(days=90),
}

def gc_pii_store():
    cutoff = datetime.now(timezone.utc) - RETENTION["pii_store"]
    pii_store.delete_where(lambda r: r["created_at"] < cutoff)
