"""table bill

Revision ID: 4e5e472ba38c
Revises: e3e0801a51aa
Create Date: 2024-08-20 13:55:15.860357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e5e472ba38c'
down_revision = 'e3e0801a51aa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plate', sa.String(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bill_created'), 'bill', ['created'], unique=False)
    op.create_index(op.f('ix_bill_end_time'), 'bill', ['end_time'], unique=False)
    op.create_index(op.f('ix_bill_id'), 'bill', ['id'], unique=False)
    op.create_index(op.f('ix_bill_is_deleted'), 'bill', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_bill_modified'), 'bill', ['modified'], unique=False)
    op.create_index(op.f('ix_bill_price'), 'bill', ['price'], unique=False)
    op.create_index(op.f('ix_bill_start_time'), 'bill', ['start_time'], unique=False)
    op.create_index(op.f('ix_bill_status'), 'bill', ['status'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bill_status'), table_name='bill')
    op.drop_index(op.f('ix_bill_start_time'), table_name='bill')
    op.drop_index(op.f('ix_bill_price'), table_name='bill')
    op.drop_index(op.f('ix_bill_modified'), table_name='bill')
    op.drop_index(op.f('ix_bill_is_deleted'), table_name='bill')
    op.drop_index(op.f('ix_bill_id'), table_name='bill')
    op.drop_index(op.f('ix_bill_end_time'), table_name='bill')
    op.drop_index(op.f('ix_bill_created'), table_name='bill')
    op.drop_table('bill')
    # ### end Alembic commands ###
