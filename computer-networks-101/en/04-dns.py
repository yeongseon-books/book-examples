"""Computer Networks 101 - Episode 4: Dns."""

# English mirror of the corresponding episode demo
from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    """Record."""

    rtype: str
    value: str


ZONE = {
    ".": {"com": Record("NS", "a.gtld-servers.local")},
    "com": {"example": Record("NS", "ns1.example.local")},
    "example.com": {
        "@": Record("A", "93.184.216.34"),
        "www": Record("CNAME", "example.com"),
    },
}


def resolve(name: str, rtype: str = "A") -> str:
    """Resolve."""
    if name == "www.example.com":
        cname = ZONE["example.com"]["www"]
        if cname.rtype == "CNAME":
            return resolve(cname.value, rtype)
    if name == "example.com":
        rec = ZONE["example.com"]["@"]
        if rec.rtype == rtype:
            return rec.value
    raise KeyError(f"no record for {name} {rtype}")


def recursive_path(name: str) -> list[str]:
    """Recursive path."""
    return [".", "com", "example.com", name]


if __name__ == "__main__":
    print(resolve("www.example.com"))
