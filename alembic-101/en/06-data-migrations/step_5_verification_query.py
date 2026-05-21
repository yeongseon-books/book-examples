"""Generated from book-content article."""

def upgrade() -> None:
    bind = op.get_bind()
    # ... backfill work ...
    remaining = bind.execute(text("SELECT COUNT(*) FROM users WHERE tier IS NULL")).scalar()
    assert remaining == 0, f"backfill incomplete: {remaining} rows remain"
