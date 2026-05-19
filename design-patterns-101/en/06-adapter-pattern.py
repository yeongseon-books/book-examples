"""Design Patterns 101 - Episode 6: Adapter pattern."""

import json


class LegacyXmlLogger:
    """Legacy xml logger."""

    def write_xml(self, event, level):
        """Write xml."""
        return f"<log><event>{event}</event><level>{level}</level></log>"


class JsonLogger:
    """Json logger."""

    def write_json(self, event, level):
        """Write json."""
        return json.dumps({"event": event, "level": level}, sort_keys=True)


class LoggerTarget:
    """Logger target."""

    def log(self, event, level):
        """Log."""
        raise NotImplementedError


class XmlLoggerAdapter(LoggerTarget):
    """Xml logger adapter."""

    def __init__(self, legacy):
        self.legacy = legacy

    def log(self, event, level):
        """Log."""
        xml = self.legacy.write_xml(event, level)
        return {"event": event, "level": level, "raw": xml}


class JsonLoggerAdapter(LoggerTarget):
    """Json logger adapter."""

    def __init__(self, modern):
        self.modern = modern

    def log(self, event, level):
        """Log."""
        payload = self.modern.write_json(event, level)
        return {"event": event, "level": level, "raw": payload}
