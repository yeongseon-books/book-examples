"""Generated from book-content article."""

import secrets
from dataclasses import dataclass, field


@dataclass
class PIITokenizer:
    mapping: dict[str, str] = field(default_factory=dict)
    reverse: dict[str, str] = field(default_factory=dict)

    def tokenize(self, text: str, detected: list[tuple]) -> str:
        # Iterate in reverse order so offsets stay valid
        for cat, start, end, value in sorted(detected, key=lambda x: -x[1]):
            if value not in self.mapping:
                token = f"<{cat.upper()}_{secrets.token_hex(4)}>"
                self.mapping[value] = token
                self.reverse[token] = value
            text = text[:start] + self.mapping[value] + text[end:]
        return text

    def detokenize(self, text: str) -> str:
        for token, value in self.reverse.items():
            text = text.replace(token, value)
        return text

tk = PIITokenizer()
src = "Alice (alice@example.com) ordered. Send to alice@example.com."
detected = detect_pii(src)
masked = tk.tokenize(src, detected)
# "Alice (<EMAIL_a3b2c1d0>) ordered. Send to <EMAIL_a3b2c1d0>."
# Same email maps to the same token → model treats it as one entity.

response = llm.complete(masked)
final = tk.detokenize(response)  # restore before sending to user
