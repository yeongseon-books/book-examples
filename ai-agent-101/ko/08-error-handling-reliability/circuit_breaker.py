"""Generated from book-content article."""

from enum import Enum
import time

class CircuitState(Enum):
    CLOSED = "closed"      # normal
    OPEN = "open"          # blocked
    HALF_OPEN = "half_open"  # trial calls
