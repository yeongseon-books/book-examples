# pip install tiktoken
import tiktoken


def count_tokens(text: str, model: str = "gpt-4o") -> int:
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

samples = {
    "english": "The quick brown fox jumps over the lazy dog.",
    "korean": "빠른 갈색 여우가 게으른 개를 뛰어넘는다.",
    "code": "def add(a, b):\n    return a + b",
}
for name, text in samples.items():
    n = count_tokens(text)
    chars = len(text)
    print(f"{name:8s} chars={chars:3d} tokens={n:3d} ratio={chars/n:.2f}")
