"""Generated from book-content article."""

self.blocks = nn.ModuleList([Block(config) for _ in range(config.n_layer)])

for block in self.blocks:
    x = block(x)
