"""Generated from book-content article."""

def store_audit(record: AuditRecord, prompt: str, response: str):
    # 1. Audit log: append-only, hashes only
    audit_db.insert(asdict(record))

    # 2. PII store: KMS encrypted, short retention based on user consent
    if user_consent_to_train(record.user_id_hash):
        encrypted_prompt = kms.encrypt(prompt)
        encrypted_response = kms.encrypt(response)
        pii_store.put(record.request_id, {
            "prompt": encrypted_prompt,
            "response": encrypted_response,
            "ttl": 90,  # days
        })
