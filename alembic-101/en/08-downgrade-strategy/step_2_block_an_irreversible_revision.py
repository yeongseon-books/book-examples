"""Generated from book-content article."""

def upgrade() -> None:
    op.drop_column("users", "old_field")

def downgrade() -> None:
    raise NotImplementedError("drop is irreversible (data loss)")
