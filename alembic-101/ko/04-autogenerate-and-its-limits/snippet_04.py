# After: hand-edited to a real rename
def upgrade() -> None:
    op.alter_column("users", "name", new_column_name="display_name")

def downgrade() -> None:
    op.alter_column("users", "display_name", new_column_name="name")
