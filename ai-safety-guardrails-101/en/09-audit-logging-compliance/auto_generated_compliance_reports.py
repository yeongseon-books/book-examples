"""Generated from book-content article."""

def monthly_report(year: int, month: int) -> dict:
    rows = audit_db.query(year=year, month=month)
    return {
        "total_requests": len(rows),
        "blocked_requests": sum(1 for r in rows if r["blocked"]),
        "block_reasons": Counter(r["block_reason"] for r in rows if r["blocked"]),
        "pii_redaction_count": sum(1 for r in rows if "pii_redacted" in r["guardrail_decisions"]),
        "models_used": Counter(r["model"] for r in rows),
        "total_cost_usd": sum(r["cost_usd"] for r in rows),
        "p95_latency_ms": percentile([r["latency_ms"] for r in rows], 95),
    }
