"""Generated from book-content article."""

class UserInputError(Exception):
    pass

def validate_user_input(text: str, max_chars: int = 10000) -> str:
    """Validate user input."""
    if not text or not text.strip():
        raise UserInputError("empty input")
    if len(text) > max_chars:
        raise UserInputError(f"input too long ({len(text)} chars, max {max_chars})")
    return text.strip()
