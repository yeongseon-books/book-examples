"""Generated from book-content article."""

def upgrade() -> None:
    op.add_column("users", sa.Column("display_name", sa.String(100), nullable=True))

def downgrade() -> None:
    op.drop_column("users", "display_name")
