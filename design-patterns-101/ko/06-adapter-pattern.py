import json

class LegacyXmlLogger:
    def write_xml(self, event, level): return f'<log><event>{event}</event><level>{level}</level></log>'

class JsonLogger:
    def write_json(self, event, level): return json.dumps({'event': event, 'level': level}, sort_keys=True)

class LoggerTarget:
    def log(self, event, level): raise NotImplementedError

class XmlLoggerAdapter(LoggerTarget):
    def __init__(self, legacy): self.legacy = legacy
    def log(self, event, level):
        xml = self.legacy.write_xml(event, level)
        return {'event': event, 'level': level, 'raw': xml}

class JsonLoggerAdapter(LoggerTarget):
    def __init__(self, modern): self.modern = modern
    def log(self, event, level):
        payload = self.modern.write_json(event, level)
        return {'event': event, 'level': level, 'raw': payload}
