# Before: column rename misread as drop + add
def upgrade() -> None:
    op.add_column("users", sa.Column("display_name", sa.String(100)))
    op.drop_column("users", "name")  # ← data loss!

def downgrade() -> None:
    op.add_column("users", sa.Column("name", sa.String(100)))
    op.drop_column("users", "display_name")
