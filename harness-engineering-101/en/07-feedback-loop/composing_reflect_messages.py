"""Generated from book-content article."""

@dataclass
class ReflectMessage:
    """The bridge from failure to a new attempt."""
    attempt_number: int
    failed_action: str
    failure_reason: str
    suggested_change: str
    constraint: str

    def to_prompt(self) -> str:
        return f"""Attempt #{self.attempt_number} failed.

What you tried: {self.failed_action}
Why it failed: {self.failure_reason}
What to try next: {self.suggested_change}
Constraint for next attempt: {self.constraint}

Now produce a new attempt that satisfies the constraint."""

msg = ReflectMessage(
    attempt_number=2,
    failed_action="Called create_user with email='alice'",
    failure_reason="email field requires a valid address (must contain @)",
    suggested_change="Provide the full email like alice@example.com",
    constraint="email must match RFC 5322 format",
)
