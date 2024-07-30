"""set status record

Revision ID: 2e3a3aecbb28
Revises: 71761356f420
Create Date: 2024-07-30 10:14:43.418075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e3a3aecbb28'
down_revision = '71761356f420'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record', sa.Column('latest_status', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('record', 'latest_status')
    # ### end Alembic commands ###
