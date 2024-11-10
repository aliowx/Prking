"""add phone number into plate

Revision ID: aedacab0275f
Revises: ca6dcadd7f0a
Create Date: 2024-11-04 19:46:00.969889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aedacab0275f'
down_revision = 'ca6dcadd7f0a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('platelist', sa.Column('phone_number', sa.String(), nullable=True))
    op.create_index(op.f('ix_platelist_phone_number'), 'platelist', ['phone_number'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_platelist_phone_number'), table_name='platelist')
    op.drop_column('platelist', 'phone_number')
    # ### end Alembic commands ###