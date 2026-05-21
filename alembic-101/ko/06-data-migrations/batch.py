"""Generated from book-content article."""

def upgrade() -> None:
    bind = op.get_bind()
    batch_size = 1000
    while True:
        result = bind.execute(text(
            "UPDATE users SET tier = 'free' "
            "WHERE id IN (SELECT id FROM users WHERE tier IS NULL LIMIT :n)"
        ), {"n": batch_size})
        if result.rowcount == 0:
            break
