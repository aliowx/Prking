"""add column bill_type into Bill

Revision ID: 217829808cec
Revises: 884ff520533a
Create Date: 2024-10-21 14:19:14.688374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '217829808cec'
down_revision = '884ff520533a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bill', sa.Column('bill_type', sa.String(), nullable=True))
    op.create_index(op.f('ix_bill_bill_type'), 'bill', ['bill_type'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bill_bill_type'), table_name='bill')
    op.drop_column('bill', 'bill_type')
    # ### end Alembic commands ###
