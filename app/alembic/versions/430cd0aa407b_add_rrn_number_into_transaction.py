"""add rrn_number into transaction

Revision ID: 430cd0aa407b
Revises: 0abbceea8f6c
Create Date: 2024-11-17 11:35:49.735925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '430cd0aa407b'
down_revision = '0abbceea8f6c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('rrn_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transaction', 'rrn_number')
    # ### end Alembic commands ###
