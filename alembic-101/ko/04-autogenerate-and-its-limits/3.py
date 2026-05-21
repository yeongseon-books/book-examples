"""Generated from book-content article."""

def upgrade() -> None:
    op.add_column("users", sa.Column("tier", sa.String(length=16), server_default="free", nullable=False))

def downgrade() -> None:
    op.drop_column("users", "tier")
