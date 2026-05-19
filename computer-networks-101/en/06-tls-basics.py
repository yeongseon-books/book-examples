"""Computer Networks 101 - Episode 6: Tls basics."""

# English mirror of the corresponding episode demo
from dataclasses import dataclass

VALID_SEQUENCE = [
    "ClientHello",
    "ServerHello",
    "Certificate",
    "KeyExchange",
    "Finished",
]


@dataclass
class TLSStateMachine:
    """TLS state machine."""

    state: str = "START"
    cursor: int = 0

    def consume(self, message: str) -> str:
        """Consume."""
        if self.cursor >= len(VALID_SEQUENCE):
            raise ValueError("handshake already complete")
        expected = VALID_SEQUENCE[self.cursor]
        if message != expected:
            raise ValueError(f"expected {expected}, got {message}")
        self.cursor += 1
        if self.cursor == len(VALID_SEQUENCE):
            self.state = "APPLICATION_DATA"
        else:
            self.state = VALID_SEQUENCE[self.cursor]
        return self.state


def validate_certificate_chain(chain: list[str], trust_store: set[str]) -> bool:
    """Validate certificate chain."""
    if len(chain) < 2:
        return False
    root = chain[-1]
    return root in trust_store


if __name__ == "__main__":
    sm = TLSStateMachine()
    for item in VALID_SEQUENCE:
        _ = sm.consume(item)
    print(sm.state)
