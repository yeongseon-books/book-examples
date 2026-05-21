"""Generated from book-content article."""

def upgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.alter_column("tier", existing_type=sa.String(16), nullable=False)

def downgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.alter_column("tier", existing_type=sa.String(16), nullable=True)
