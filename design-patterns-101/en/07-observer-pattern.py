"""Design Patterns 101 - Episode 7: Observer pattern."""

import weakref


class EventBus:
    """Event bus."""

    def __init__(self):
        self._subs = {}

    def subscribe(self, topic, fn):
        """Subscribe."""
        if hasattr(fn, "__self__") and fn.__self__ is not None:
            ref = weakref.WeakMethod(fn)
            self._subs.setdefault(topic, []).append(ref)
            return ref
        ref = weakref.ref(fn)
        self._subs.setdefault(topic, []).append(ref)
        return ref

    def unsubscribe(self, topic, token):
        """Unsubscribe."""
        self._subs[topic] = [r for r in self._subs.get(topic, []) if r is not token]

    def publish(self, topic, event):
        """Publish."""
        alive = []
        for ref in self._subs.get(topic, []):
            fn = ref()
            if fn is None:
                continue
            fn(event)
            alive.append(ref)
        self._subs[topic] = alive


class Recorder:
    """Recorder."""

    def __init__(self):
        self.events = []

    def on_event(self, event):
        """On event."""
        self.events.append(event)
