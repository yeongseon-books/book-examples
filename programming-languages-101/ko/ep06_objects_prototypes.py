"""Programming Languages 101 - Episode 6: Objects prototypes."""


def create_object(proto=None, **props):
    """Create object."""
    return {"__proto__": proto, **props}


def get(obj, key):
    """Get."""
    cur = obj
    while cur is not None:
        if key in cur:
            return cur[key]
        cur = cur.get("__proto__")
    raise KeyError(key)
