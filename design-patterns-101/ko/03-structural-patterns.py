class LegacyWriter:
    def write_line(self, text): return f'legacy:{text}'
class JsonLogger:
    def log(self, text): return {'message': text}
class WriterAdapter:
    def __init__(self, legacy): self.legacy = legacy
    def log(self, text): return {'message': self.legacy.write_line(text).split(':',1)[1]}

class Renderer:
    def render(self, text): raise NotImplementedError
class PlainRenderer(Renderer):
    def render(self, text): return text
class HtmlBridge(Renderer):
    def __init__(self, impl): self.impl = impl
    def render(self, text): return f'<{self.impl}>{text}</{self.impl}>'

class Node:
    def size(self): raise NotImplementedError
class File(Node):
    def __init__(self, n): self.n=n
    def size(self): return self.n
class Folder(Node):
    def __init__(self, children): self.children=children
    def size(self): return sum(c.size() for c in self.children)

class Notifier:
    def send(self, msg): return [msg]
class TimestampDecorator(Notifier):
    def __init__(self, inner): self.inner=inner
    def send(self, msg): return self.inner.send(f'ts:{msg}')

class CheckoutFacade:
    def buy(self, user, item): return f'{user}:{item}:ok'

class DataSource:
    def __init__(self): self.calls=0
    def get(self, key): self.calls += 1; return f'v:{key}'
class CacheProxy:
    def __init__(self, real): self.real=real; self.cache={}
    def get(self, key):
        if key not in self.cache: self.cache[key]=self.real.get(key)
        return self.cache[key]
