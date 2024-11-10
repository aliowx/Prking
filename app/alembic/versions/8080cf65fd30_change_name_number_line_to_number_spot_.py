"""change name number_line to number_spot in spot

Revision ID: 8080cf65fd30
Revises: 7e4a3a5cdcfa
Create Date: 2024-07-09 10:30:05.985576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8080cf65fd30'
down_revision = '7e4a3a5cdcfa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spot', sa.Column('number_spot', sa.Integer(), nullable=True))
    op.drop_column('spot', 'number_line')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spot', sa.Column('number_line', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('spot', 'number_spot')
    # ### end Alembic commands ###