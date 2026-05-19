"""Tests for ep09 in Information Security 101."""

from common import AuditLogger


def test_audit_chain_detects_tampering():
    """Test audit chain detects tampering."""
    logger = AuditLogger(b"audit-key")
    logger.append({"actor": "a", "action": "read"})
    logger.append({"actor": "a", "action": "write"})
    assert logger.verify_chain()
    logger.records[1].event["action"] = "delete"
    assert not logger.verify_chain()
