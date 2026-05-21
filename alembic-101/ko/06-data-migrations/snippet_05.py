# After: split into three revisions
# revision 1: schema add (nullable=True)
def upgrade() -> None:
    op.add_column("users", sa.Column("tier", sa.String(16), nullable=True))

# revision 2: data backfill (batch loop)
def upgrade() -> None:
    bind = op.get_bind()
    while True:
        result = bind.execute(text(
            "UPDATE users SET tier = CASE "
            "  WHEN last_payment_at IS NOT NULL THEN 'paid' ELSE 'free' END "
            "WHERE id IN (SELECT id FROM users WHERE tier IS NULL LIMIT 1000)"
        ))
        if result.rowcount == 0:
            break

# revision 3: schema tighten
def upgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.alter_column("tier", existing_type=sa.String(16), nullable=False)
