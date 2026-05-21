"""Generated from book-content article."""

import json
import logging

log = logging.getLogger("app")

log.error(json.dumps({
    "event": "order_failed",
    "user_id": user_id,
    "error": str(e),
}))
