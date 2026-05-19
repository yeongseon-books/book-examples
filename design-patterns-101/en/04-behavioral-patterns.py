class Handler:
    def __init__(self, nxt=None): self.nxt=nxt
    def handle(self, req): return self.nxt.handle(req) if self.nxt else 'unhandled'
class AuthHandler(Handler):
    def handle(self, req): return super().handle(req) if req.get('auth') else 'unauthorized'
class RouteHandler(Handler):
    def handle(self, req): return f"route:{req['path']}"

class Command:
    def execute(self): raise NotImplementedError
class AddCommand(Command):
    def __init__(self, a,b): self.a=a; self.b=b
    def execute(self): return self.a + self.b

class Numbers:
    def __init__(self, values): self.values=values
    def __iter__(self):
        for v in self.values: yield v

class Mediator:
    def notify(self, sender, event): return f'{sender}:{event}'

class Memento:
    def __init__(self, state): self.state=state
class Originator:
    def __init__(self): self.state=''
    def save(self): return Memento(self.state)
    def restore(self, m): self.state=m.state

class DraftState:
    def submit(self): return PublishedState()
class PublishedState:
    def submit(self): return self
class Article:
    def __init__(self): self.state=DraftState()
    def submit(self): self.state=self.state.submit()

class Pipeline:
    def process(self, req): return self.parse(req) + self.transform(req)
    def parse(self, req): return ['parsed']
    def transform(self, req): return ['transformed']
