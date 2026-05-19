"""Information Security 101 - Episode 9: Logging and audit."""

from common import AuditLogger

logger = AuditLogger(b"audit-key")
logger.append({"actor": "alice", "action": "read", "resource": "report"})
logger.append({"actor": "alice", "action": "write", "resource": "report"})
print({"records": len(logger.records), "chain_ok": logger.verify_chain()})
