"""Generated from book-content article."""

def upgrade() -> None:
    op.add_column("users", sa.Column("display_name", sa.String(100)))
    op.execute("UPDATE users SET display_name = name WHERE display_name IS NULL")
