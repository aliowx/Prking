"""add price to payment

Revision ID: 6b33396f2d5f
Revises: 840f5de47436
Create Date: 2024-08-25 18:10:48.399295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b33396f2d5f'
down_revision = '840f5de47436'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('price', sa.Float(), nullable=True))
    op.create_index(op.f('ix_payment_price'), 'payment', ['price'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_payment_price'), table_name='payment')
    op.drop_column('payment', 'price')
    # ### end Alembic commands ###
