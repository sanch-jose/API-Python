"""create posts table

Revision ID: 386d4a057522
Revises: 
Create Date: 2023-01-16 16:30:06.652530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '386d4a057522'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass