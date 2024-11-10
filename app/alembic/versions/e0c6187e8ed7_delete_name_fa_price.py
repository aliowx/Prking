"""delete name_fa price

Revision ID: e0c6187e8ed7
Revises: eae0c509654e
Create Date: 2024-09-01 16:23:15.725889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0c6187e8ed7'
down_revision = 'eae0c509654e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('price', 'name_fa')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('price', sa.Column('name_fa', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###