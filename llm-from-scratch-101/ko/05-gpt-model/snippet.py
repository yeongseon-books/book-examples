"""Generated from book-content article."""

config = GPTConfig()
model = GPT(config)
num_params = sum(p.numel() for p in model.parameters())
print(f"params: {num_params:,}")
