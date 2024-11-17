"""add table transaction

Revision ID: d1ed1a9658ae
Revises: d78ddc5d33db
Create Date: 2024-11-13 20:33:16.591244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1ed1a9658ae'
down_revision = 'd78ddc5d33db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bill_ids', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('order_id', sa.BigInteger(), nullable=True),
    sa.Column('amount', sa.BigInteger(), nullable=True),
    sa.Column('callback_url', sa.String(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_id')
    )
    op.create_index(op.f('ix_transaction_created'), 'transaction', ['created'], unique=False)
    op.create_index(op.f('ix_transaction_id'), 'transaction', ['id'], unique=False)
    op.create_index(op.f('ix_transaction_is_deleted'), 'transaction', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_transaction_modified'), 'transaction', ['modified'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transaction_modified'), table_name='transaction')
    op.drop_index(op.f('ix_transaction_is_deleted'), table_name='transaction')
    op.drop_index(op.f('ix_transaction_id'), table_name='transaction')
    op.drop_index(op.f('ix_transaction_created'), table_name='transaction')
    op.drop_table('transaction')
    # ### end Alembic commands ###