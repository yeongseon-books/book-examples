"""Generated from book-content article."""

import json
import logging
from datetime import datetime
from typing import Any


class StructuredLogger:
    """Structured logger."""

    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(message)s"))
        self.logger.addHandler(handler)

    def log(self, level: str, event: str, **fields):
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "event": event,
            **fields
        }
        self.logger.info(json.dumps(record, default=str))

    def info(self, event: str, **fields):
        self.log("INFO", event, **fields)

    def error(self, event: str, **fields):
        self.log("ERROR", event, **fields)
