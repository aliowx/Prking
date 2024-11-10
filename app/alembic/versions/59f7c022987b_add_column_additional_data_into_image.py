"""add column additional_data into image

Revision ID: 59f7c022987b
Revises: f2bc3fcf6b81
Create Date: 2024-10-30 14:28:47.137400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59f7c022987b'
down_revision = 'f2bc3fcf6b81'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('additonal_data', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'additonal_data')
    # ### end Alembic commands ###