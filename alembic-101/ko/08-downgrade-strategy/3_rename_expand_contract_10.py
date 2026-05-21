"""Generated from book-content article."""

def upgrade() -> None:
    op.drop_column("users", "name")

def downgrade() -> None:
    raise NotImplementedError("drop name is irreversible")
