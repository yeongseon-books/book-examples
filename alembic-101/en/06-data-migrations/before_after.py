# Before: schema and data bundled into one revision and timing out
def upgrade() -> None:
    op.add_column("users", sa.Column("tier", sa.String(16), nullable=False, server_default="free"))
    # 100M-row UPDATE — lock + transaction log explosion
    op.execute("UPDATE users SET tier = 'paid' WHERE last_payment_at IS NOT NULL")
    op.alter_column("users", "tier", server_default=None)
