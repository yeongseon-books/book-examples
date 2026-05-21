# Before: empty downgrade on an irreversible change
def upgrade() -> None:
    op.drop_column("users", "legacy_token")  # ← data lost forever

def downgrade() -> None:
    pass  # ← silently "succeeds" on accident
