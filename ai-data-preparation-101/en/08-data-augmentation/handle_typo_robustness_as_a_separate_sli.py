"""Generated from book-content article."""

import random


def inject_typo(text: str, p: float = 0.08) -> str:
    chars = list(text)
    for i in range(len(chars) - 1):
        if random.random() < p and chars[i].isalnum() and chars[i + 1].isalnum():
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
            break
    return "".join(chars)

print(inject_typo("환불이 아직 안 됐는데 언제 처리되나요?"))
