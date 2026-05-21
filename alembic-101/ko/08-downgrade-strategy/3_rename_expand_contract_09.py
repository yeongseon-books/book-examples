"""Generated from book-content article."""

def upgrade() -> None:
    bind = op.get_bind()
    bind.execute(text("UPDATE users SET display_name = name WHERE display_name IS NULL"))

def downgrade() -> None:
    raise NotImplementedError("data migration is irreversible")
