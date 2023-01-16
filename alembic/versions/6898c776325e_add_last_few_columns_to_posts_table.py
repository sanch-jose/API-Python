"""add last few columns to posts table

Revision ID: 6898c776325e
Revises: 2e634a3e4208
Create Date: 2023-01-16 16:33:56.657960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6898c776325e'
down_revision = '2e634a3e4208'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass