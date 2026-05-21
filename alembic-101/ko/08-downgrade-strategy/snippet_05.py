# After: explicit block
def upgrade() -> None:
    op.drop_column("users", "legacy_token")

def downgrade() -> None:
    raise NotImplementedError(
        "drop column users.legacy_token is irreversible (data loss). "
        "Restore from backup or apply a new revision that re-adds the column."
    )
