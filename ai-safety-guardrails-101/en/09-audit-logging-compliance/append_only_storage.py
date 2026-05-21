"""Generated from book-content article."""

from hashlib import sha256


def chain_hash(prev_hash: str, record: dict) -> str:
    payload = prev_hash + str(sorted(record.items()))
    return sha256(payload.encode()).hexdigest()

def append_with_chain(record: dict):
    prev = audit_db.last_hash() or "0" * 64
    record["prev_hash"] = prev
    record["self_hash"] = chain_hash(prev, record)
    audit_db.insert(record)
