"""Generated from book-content article."""

import hashlib
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass
class AuditRecord:
    request_id: str
    timestamp: str
    user_id_hash: str          # PII becomes a hash
    api_key_id: str
    model: str
    input_token_count: int
    output_token_count: int
    cost_usd: float
    guardrail_decisions: list  # ["pii_redacted", "moderation_passed", ...]
    blocked: bool
    block_reason: str | None
    prompt_hash: str           # raw text lives in a separate store
    response_hash: str
    retrieved_chunk_ids: list[int]
    latency_ms: int

def make_record(user_id: str, prompt: str, response: str, **kw) -> AuditRecord:
    return AuditRecord(
        request_id=str(uuid.uuid4()),
        timestamp=datetime.now(timezone.utc).isoformat(),
        user_id_hash=hashlib.sha256(user_id.encode()).hexdigest()[:16],
        prompt_hash=hashlib.sha256(prompt.encode()).hexdigest(),
        response_hash=hashlib.sha256(response.encode()).hexdigest(),
        **kw,
    )
