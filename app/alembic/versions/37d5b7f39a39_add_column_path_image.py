"""add column path_image

Revision ID: 37d5b7f39a39
Revises: f133f0ef1fe6
Create Date: 2024-10-17 11:00:44.704987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37d5b7f39a39'
down_revision = 'f133f0ef1fe6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('path_image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'path_image')
    # ### end Alembic commands ###
