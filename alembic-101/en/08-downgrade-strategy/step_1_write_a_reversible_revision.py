"""Generated from book-content article."""

def upgrade() -> None:
    op.add_column("users", sa.Column("nickname", sa.String(50), nullable=True))

def downgrade() -> None:
    op.drop_column("users", "nickname")
