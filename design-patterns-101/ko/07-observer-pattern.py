import weakref


class EventBus:
    def __init__(self):
        self._subs = {}

    def subscribe(self, topic, fn):
        if hasattr(fn, "__self__") and fn.__self__ is not None:
            ref = weakref.WeakMethod(fn)
            self._subs.setdefault(topic, []).append(ref)
            return ref
        ref = weakref.ref(fn)
        self._subs.setdefault(topic, []).append(ref)
        return ref

    def unsubscribe(self, topic, token):
        self._subs[topic] = [r for r in self._subs.get(topic, []) if r is not token]

    def publish(self, topic, event):
        alive = []
        for ref in self._subs.get(topic, []):
            fn = ref()
            if fn is None:
                continue
            fn(event)
            alive.append(ref)
        self._subs[topic] = alive


class Recorder:
    def __init__(self):
        self.events = []

    def on_event(self, event):
        self.events.append(event)
