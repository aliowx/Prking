"""add transaction number

Revision ID: dda6e26d3b69
Revises: be2e7debdfda
Create Date: 2024-11-19 09:49:21.533531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dda6e26d3b69'
down_revision = 'be2e7debdfda'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('transaction_number', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_transaction_transaction_number'), 'transaction', ['transaction_number'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transaction_transaction_number'), table_name='transaction')
    op.drop_column('transaction', 'transaction_number')
    # ### end Alembic commands ###
