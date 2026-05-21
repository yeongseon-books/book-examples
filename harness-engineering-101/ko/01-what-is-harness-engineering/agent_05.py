"""Generated from book-content article."""

from enum import Enum
from pydantic import BaseModel, Field

class Priority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class ClassificationResult(BaseModel):
    """Test Harness: schema pins down completion criteria."""
    priority: Priority
    reason: str = Field(..., min_length=10)
    confidence: float = Field(..., ge=0.0, le=1.0)

SYSTEM_PROMPT = """You are an email priority classifier.

Classification criteria (Context Harness):
- high: response required within 24 hours. Customer complaints, payment failures, security issues.
- medium: response required within 3 business days. General inquiries, feature requests.
- low: response optional. Marketing, notifications, automated emails.

Rules (Constraint Harness):
- Use only one of the three categories above.
- Reason must be a single sentence explaining the basis for the label.
- Confidence must be a number between 0.0 and 1.0.
- Do not infer information not present in the email body."""

def classify_email_with_harness(email_body: str) -> ClassificationResult:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": email_body},
        ],
        response_format=ClassificationResult,  # Test Harness
    )
    return ClassificationResult.model_validate_json(response.choices[0].message.content)
