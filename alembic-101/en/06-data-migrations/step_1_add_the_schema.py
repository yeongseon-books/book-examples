"""Generated from book-content article."""

def upgrade() -> None:
    op.add_column("users", sa.Column("tier", sa.String(16), nullable=True))

def downgrade() -> None:
    op.drop_column("users", "tier")
