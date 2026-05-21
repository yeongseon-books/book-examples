"""Generated from book-content article."""

def upgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.add_column(sa.Column("tier", sa.String(16), nullable=False, server_default="free"))

def downgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.drop_column("tier")
