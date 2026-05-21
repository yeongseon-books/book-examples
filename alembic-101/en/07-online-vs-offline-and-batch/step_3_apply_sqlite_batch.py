"""Generated from book-content article."""

def upgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.alter_column("tier",
                           existing_type=sa.String(16),
                           type_=sa.String(64))
        batch.create_index("ix_users_tier", ["tier"])
