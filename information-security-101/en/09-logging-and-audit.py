"""Information Security 101 - Episode 9: Logging and audit."""

from common import AuditLogger

logger = AuditLogger(b"audit-key")
logger.append({"actor": "bob", "action": "login", "result": "ok"})
logger.append({"actor": "bob", "action": "logout", "result": "ok"})
print({"chain_ok": logger.verify_chain()})
