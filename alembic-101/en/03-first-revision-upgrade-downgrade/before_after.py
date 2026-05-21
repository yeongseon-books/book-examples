# Before: a dangerous revision with empty downgrade
def upgrade() -> None:
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("amount", sa.Numeric(10, 2), nullable=False),
    )
    op.create_index("ix_orders_user_id", "orders", ["user_id"])

def downgrade() -> None:
    pass  # ← leaving this empty makes it a one-way commit
