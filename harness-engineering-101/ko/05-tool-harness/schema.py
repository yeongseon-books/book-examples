"""Generated from book-content article."""

from pydantic import BaseModel, Field, model_validator
from typing import Literal

class SendNotificationInput(BaseModel):
    """Send a notification."""
    channel: Literal["email", "sms", "push"] = Field(
        ...,
        description="Send channel. email needs an email address; sms needs a phone number.",
    )
    recipient: str = Field(..., description="Recipient identifier (varies by channel)")
    template_id: str = Field(..., pattern=r"^TPL-\d{4}$", description="Format: TPL-0001")
    variables: dict[str, str] = Field(
        default_factory=dict,
        description="Template variables. Example: {'name': 'Alice', 'order_id': '12345'}",
    )

    @model_validator(mode="after")
    def validate_recipient_format(self):
        if self.channel == "email" and "@" not in self.recipient:
            raise ValueError(f"channel=email requires email address, got: {self.recipient}")
        if self.channel == "sms" and not self.recipient.startswith("+"):
            raise ValueError(f"channel=sms requires E.164 phone (+countrycode), got: {self.recipient}")
        return self
