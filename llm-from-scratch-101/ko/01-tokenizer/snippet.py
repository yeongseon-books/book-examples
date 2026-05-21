"""Generated from book-content article."""

text = "hello world"
chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}

def encode(s: str) -> list[int]:
    dropped = sorted({c for c in s if c not in stoi})
    if dropped:
        print(f"dropped unsupported characters: {dropped}")
    return [stoi[c] for c in s if c in stoi]

def decode(ids):
    return "".join(itos[i] for i in ids)

ids = encode(text)
print(ids)
print(decode(ids))
