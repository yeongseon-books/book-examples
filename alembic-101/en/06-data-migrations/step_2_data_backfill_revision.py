"""Generated from book-content article."""

from sqlalchemy import text

def upgrade() -> None:
    bind = op.get_bind()
    batch = 1000
    while True:
        result = bind.execute(text(
            "UPDATE users SET tier = 'free' "
            "WHERE id IN (SELECT id FROM users WHERE tier IS NULL LIMIT :n)"
        ), {"n": batch})
        if result.rowcount == 0:
            break

def downgrade() -> None:
    pass  # data migrations usually do not roll back (raise NotImplementedError is also fine)
