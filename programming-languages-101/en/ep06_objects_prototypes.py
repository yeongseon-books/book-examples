def create_object(proto=None, **props):
    return {"__proto__": proto, **props}


def get(obj, key):
    cur = obj
    while cur is not None:
        if key in cur:
            return cur[key]
        cur = cur.get("__proto__")
    raise KeyError(key)
