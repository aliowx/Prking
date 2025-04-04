"""add column combined_record_ids into record

Revision ID: 725407b4fc3a
Revises: 201935381731
Create Date: 2024-11-26 13:52:50.826987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '725407b4fc3a'
down_revision = '201935381731'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record', sa.Column('combined_record_ids', sa.ARRAY(sa.Integer()), server_default='{}', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('record', 'combined_record_ids')
    # ### end Alembic commands ###
