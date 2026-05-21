"""Generated from book-content article."""

def upgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.alter_column("name", new_column_name="display_name")

def downgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.alter_column("display_name", new_column_name="name")
