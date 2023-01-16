"""add content column to posts table

Revision ID: 7ac1fa0b5f95
Revises: 386d4a057522
Create Date: 2023-01-16 16:31:22.304904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ac1fa0b5f95'
down_revision = '386d4a057522'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
