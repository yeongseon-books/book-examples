"""Generated from book-content article."""

import time
from enum import Enum


class CircuitState(Enum):
    CLOSED = "closed"      # normal
    OPEN = "open"          # blocked
    HALF_OPEN = "half_open"  # trial calls
