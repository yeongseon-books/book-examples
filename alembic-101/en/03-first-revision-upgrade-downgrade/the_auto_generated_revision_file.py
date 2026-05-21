"""add users.tier

Revision ID: 3f9c8b21de7a
Revises: 1a2b3c4d5e6f
Create Date: 2026-05-03 10:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

revision = "3f9c8b21de7a"
down_revision = "1a2b3c4d5e6f"
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column("users", sa.Column("tier", sa.String(16), nullable=False, server_default="free"))

def downgrade() -> None:
    op.drop_column("users", "tier")
